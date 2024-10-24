from collections.abc import Sequence
from typing import cast

from sqlalchemy.orm import contains_eager

from polar.benefit.benefits.downloadables import BenefitDownloadablesService
from polar.benefit.schemas import BenefitDownloadablesCreateProperties
from polar.models import Benefit, Downloadable, File, Organization, Product, User
from polar.models.benefit import BenefitDownloadables, BenefitType
from polar.models.benefit_grant import BenefitGrantDownloadablesProperties
from polar.models.subscription import SubscriptionStatus
from polar.postgres import AsyncSession, sql
from polar.redis import Redis
from tests.fixtures.database import SaveFixture
from tests.fixtures.random_objects import (
    create_benefit,
    create_benefit_grant,
    create_subscription,
)


class TestDownloadable:
    @classmethod
    async def create_benefit_and_grant(
        cls,
        session: AsyncSession,
        redis: Redis,
        save_fixture: SaveFixture,
        user: User,
        organization: Organization,
        product: Product,
        properties: BenefitDownloadablesCreateProperties,
    ) -> tuple[BenefitDownloadables, BenefitGrantDownloadablesProperties]:
        benefit = await create_benefit(
            save_fixture,
            type=BenefitType.downloadables,
            organization=organization,
            properties=properties.model_dump(mode="json"),
        )
        return await cls.create_grant(
            session,
            redis,
            save_fixture,
            cast(BenefitDownloadables, benefit),
            user=user,
            product=product,
        )

    @classmethod
    async def create_grant(
        cls,
        session: AsyncSession,
        redis: Redis,
        save_fixture: SaveFixture,
        benefit: BenefitDownloadables,
        user: User,
        product: Product,
    ) -> tuple[BenefitDownloadables, BenefitGrantDownloadablesProperties]:
        subscription = await create_subscription(
            save_fixture,
            product=product,
            user=user,
            status=SubscriptionStatus.active,
        )
        await create_benefit_grant(
            save_fixture,
            user,
            benefit,
            subscription=subscription,
        )
        return await cls.run_grant_task(session, redis, benefit, user)

    @classmethod
    async def run_grant_task(
        cls,
        session: AsyncSession,
        redis: Redis,
        benefit: BenefitDownloadables,
        user: User,
    ) -> tuple[BenefitDownloadables, BenefitGrantDownloadablesProperties]:
        service = BenefitDownloadablesService(session, redis)
        granted = await service.grant(benefit, user, {})
        return benefit, granted

    @classmethod
    async def run_revoke_task(
        cls,
        session: AsyncSession,
        redis: Redis,
        benefit: BenefitDownloadables,
        user: User,
    ) -> tuple[BenefitDownloadables, BenefitGrantDownloadablesProperties]:
        service = BenefitDownloadablesService(session, redis)
        revoked = await service.revoke(benefit, user, {})
        return benefit, revoked

    @classmethod
    async def get_user_downloadables(
        cls, session: AsyncSession, user: User
    ) -> Sequence[Downloadable]:
        statement = (
            sql.select(Downloadable)
            .join(File)
            .join(Benefit)
            .options(contains_eager(Downloadable.file))
            .where(
                Downloadable.user_id == user.id,
                File.deleted_at.is_(None),
                File.is_uploaded == True,  # noqa
                File.is_enabled == True,  # noqa
                Benefit.deleted_at.is_(None),
            )
        )

        res = await session.execute(statement)
        downloadables = res.scalars().all()
        return downloadables
