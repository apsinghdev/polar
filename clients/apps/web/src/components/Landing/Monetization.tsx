'use client'

import {
  AttachMoneyOutlined,
  DiamondOutlined,
  FileDownloadOutlined,
  HiveOutlined,
  StickyNote2Outlined,
  TuneOutlined,
  VerifiedOutlined,
} from '@mui/icons-material'
import Link from 'next/link'
import Avatar from 'polarkit/components/ui/atoms/avatar'
import { twMerge } from 'tailwind-merge'
import { DiscordIcon } from '../Benefit/utils'
import GitHubIcon from '../Icons/GitHubIcon'
import SubscriptionTierCard from '../Subscriptions/SubscriptionTierCard'
import FeatureItem from './molecules/FeatureItem'
import { MOCKED_PRODUCTS } from './utils'

interface BenefitCardProps {
  className: string
  title: string
  description: string
  icon: JSX.Element
}

const BenefitCard = ({
  className,
  title,
  description,
  icon,
}: BenefitCardProps) => {
  return (
    <div
      className={twMerge(
        'hover:bg-gray-75 dark:hover:bg-polar-900 dark:bg-polar-950 flex flex-col justify-between gap-y-8 bg-white p-8 transition-colors',
        className,
      )}
    >
      <span>{icon}</span>
      <div className="flex flex-col gap-y-2">
        <h3>{title}</h3>
        <p className="dark:text-polar-200 text-gray-500">{description}</p>
      </div>
    </div>
  )
}

const Benefits = () => {
  return (
    <>
      <div className="flex flex-col items-center gap-y-4">
        <h1 className="text-center text-4xl">Powerful & built-in benefits</h1>
        <p className="dark:text-polar-200 text-center text-xl text-gray-500">
          We&apos;re building common developer upsells so you don&apos;t have
          to.
        </p>
      </div>
      <div className="grid grid-cols-1 overflow-hidden rounded-3xl border md:grid-cols-3">
        <BenefitCard
          className="border-b md:border-r"
          icon={<GitHubIcon width={30} height={30} />}
          title="Private GitHub Repositories"
          description="Automate access to an unlimited amount of private GitHub repositories."
        />
        <BenefitCard
          className="border-b md:border-r"
          icon={
            <FileDownloadOutlined className="text-4xl" fontSize="inherit" />
          }
          title="File Downloads"
          description="From e-books, source code to executibles - any file is supported up to 10GB/each."
        />
        <BenefitCard
          className="border-b md:border-r"
          icon={<StickyNote2Outlined className="text-4xl" fontSize="inherit" />}
          title="Free & Premium Newsletters"
          description="Write a free, premium or early access newsletter in GitHub flavoured markdown."
        />
        <BenefitCard
          className="border-b md:border-r"
          icon={<DiscordIcon size={30} />}
          title="Discord Invites & Roles"
          description="Give customers exclusive access or premium appearances and permissions."
        />
        <BenefitCard
          className="border-b md:border-b-0 md:border-r"
          icon={<VerifiedOutlined className="text-4xl" fontSize="inherit" />}
          title="Sponsor Promotion"
          description="Automate README.md logotypes and offer newsletter sponsorship."
        />
        <BenefitCard
          icon={<TuneOutlined className="text-4xl" fontSize="inherit" />}
          title="Custom Benefit"
          description="Create your own and share secret notes, e.g Cal.com link to book consultation."
        />
      </div>
      <div className="-mt-12 text-center">
        <p className="inline-block rounded-2xl border border-gray-300 px-4 py-1 text-gray-500 dark:border-gray-800 dark:text-gray-600">
          + License keys, private packages and more to come
        </p>
      </div>
    </>
  )
}

export const Monetization = () => {
  return (
    <>
      <div className="flex flex-col gap-y-24">
        <div className="flex flex-col gap-y-4">
          <h2 className="text-4xl leading-snug md:text-5xl">
            From first donation to IPO
          </h2>
          <h3 className="dark:text-polar-600 text-4xl leading-snug text-gray-500">
            Polar offers features to scale with your needs.
          </h3>
        </div>
        <div className="grid grid-cols-1 gap-8 md:grid-cols-3">
          <FeatureItem
            className="md:row-span-2"
            icon={<DiamondOutlined />}
            title="Products & Subscriptions"
            description="Start offering developer first products and services in minutes - paid once, monthly or annually."
            link="/docs/overview/subscriptions"
          >
            <SubscriptionTierCard
              className="dark:bg-polar-900 dark:border-polar-800 border-transparent bg-white shadow-sm"
              subscriptionTier={MOCKED_PRODUCTS[1]}
            />
          </FeatureItem>
          <FeatureItem
            className="md:col-span-2"
            icon={<GitHubIcon width={20} height={20} />}
            title="Issue Funding & Rewards"
            description="Crowdfunded backlog or community bounties with seamless support to split funds with contributors."
            link="/issue-funding"
          >
            <picture>
              <source
                media="(prefers-color-scheme: dark)"
                srcSet={`/assets/landing/fund_dark.svg`}
              />
              <img
                className="dark:border-polar-700 rounded-2xl border border-gray-100"
                srcSet={`/assets/landing/fund.svg`}
                alt="Polar crowdfunding badge embedded on a GitHub issue"
              />
            </picture>
          </FeatureItem>
          <FeatureItem
            className="md:col-span-1"
            icon={<AttachMoneyOutlined />}
            title="Donations"
            description="Get appreciation from your community for a great newsletter, release or ongoing development."
            link="/docs/overview/donations"
          />
          <FeatureItem
            icon={<HiveOutlined />}
            title="Custom Integrations & SaaS"
            description="Use our API & SDK to integrate Polar across your docs, sites, apps or services."
            link="#integrations"
          />
        </div>

        <Benefits />

        <div className="flex flex-col items-center gap-y-4">
          <h1 className="text-center text-4xl">Supporting all use cases</h1>
          <p className="dark:text-polar-200 text-center text-xl text-gray-500">
            From sustainable open source, sponsorware to full-fledged SaaS.
          </p>
        </div>
        <div className="flex flex-col divide-y overflow-hidden rounded-3xl border md:flex-row md:divide-x md:divide-y-0">
          {[
            {
              name: 'Serenity OS',
              username: '@serenityos',
              avatar: 'https://avatars.githubusercontent.com/u/50811782?v=4',
              text: 'Using Polar with Issue Funding to promote rewards for contributors.',
              link: 'https://polar.sh/serenityos',
            },
            {
              name: 'Capawesome',
              username: '@capawesome-team',
              avatar: 'https://avatars.githubusercontent.com/u/105555861?v=4',
              text: 'Offering early access to sponsors using Subscription Tiers.',
              link: 'https://polar.sh/capawesome-team',
            },
            {
              name: 'Your Next Store',
              username: '@yournextstore',
              avatar: 'https://avatars.githubusercontent.com/u/159799280?v=4',
              text: 'Selling e-commerce starter kit using Polar Products & Subscriptions.',
              link: 'https://polar.sh/yournextstore',
            },
          ].map((testamonial) => (
            <Link
              key={testamonial.name}
              className="hover:bg-gray-75 dark:hover:bg-polar-900 group relative flex flex-col transition-colors md:w-1/3"
              href={testamonial.link}
              target="_blank"
            >
              <div className=" flex h-full w-full flex-col gap-y-8 rounded-none border-none p-10">
                <div className="flex flex-row items-center gap-4 space-y-0">
                  <Avatar
                    className="h-12 w-12"
                    avatar_url={testamonial.avatar}
                    name={testamonial.name}
                  />
                  <div className="flex flex-col">
                    <span>{testamonial.name}</span>
                    <span className="dark:text-polar-500 text-sm text-gray-500">
                      {testamonial.username}
                    </span>
                  </div>
                </div>
                <div className="flex h-full flex-col gap-y-4 leading-relaxed">
                  {testamonial.text}
                </div>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </>
  )
}