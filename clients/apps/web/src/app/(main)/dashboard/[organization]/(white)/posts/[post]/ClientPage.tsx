'use client'

import revalidate from '@/app/actions'
import { PostEditor } from '@/components/Feed/PostEditor'
import { DashboardBody } from '@/components/Layout/DashboardLayout'
import Spinner from '@/components/Shared/Spinner'
import { useAlertIfUnsaved } from '@/hooks/editor'
import { useArticleBySlug, useUpdateArticle } from '@/hooks/queries'
import { MaintainerOrganizationContext } from '@/providers/maintainerOrganization'
import { organizationPageLink } from '@/utils/nav'
import { usePostHog } from '@/hooks/posthog'
import { ArrowUpRightIcon } from '@heroicons/react/24/solid'
import { ArticleVisibility } from '@polar-sh/sdk'
import { AnimatePresence, motion } from 'framer-motion'
import Link from 'next/link'
import { redirect, useParams, useRouter } from 'next/navigation'
import Button from 'polarkit/components/ui/atoms/button'
import { Tabs } from 'polarkit/components/ui/atoms/tabs'
import { Banner } from 'polarkit/components/ui/molecules'
import { useCallback, useContext, useEffect, useRef, useState } from 'react'

const ClientPage = () => {
  const posthog = usePostHog()
  const params = useParams()
  const orgContext = useContext(MaintainerOrganizationContext)
  const post = useArticleBySlug(
    orgContext?.organization?.id,
    params?.post as string,
  )
  const [animateSaveBanner, setAnimateSaveBanner] = useState(false)
  const [tab, setTab] = useState(
    typeof window !== 'undefined' &&
      window &&
      window.location.hash === '#settings'
      ? 'settings'
      : 'edit',
  )

  useEffect(() => {
    if (
      typeof window !== 'undefined' &&
      window &&
      window.location.hash === '#settings'
    ) {
      setTab('settings')
    }
  }, [params])

  const router = useRouter()

  const [localArticle, setLocalArticle] = useState<{
    title: string
    body: string
  }>({
    title: '',
    body: '',
  })

  // On data load from server, populate updateArticle
  // Only do this once. After the first load, the "source of truth" for this page is the data in the browser
  const didSetPostOnLoad = useRef(false)
  useEffect(() => {
    if (didSetPostOnLoad.current) {
      return
    }
    if (!post.isFetched) {
      return
    }
    didSetPostOnLoad.current = true
    setLocalArticle({
      body: post.data?.body || '',
      title: post.data?.title || '',
    })
  }, [post.isFetched, post.data])

  const localHasDiff =
    localArticle.title !== post.data?.title ||
    localArticle.body !== post.data?.body

  const update = useUpdateArticle()

  useAlertIfUnsaved(localHasDiff)

  const handleSave = useCallback(
    async (showBanner = true) => {
      if (!post?.data?.id) {
        return
      }

      try {
        await update.mutateAsync({
          id: post.data.id,
          articleUpdate: localArticle,
        })

        // Invalidate cache on storefronts
        revalidate(`articles:${post.data.organization_id}:${post.data.slug}`)

        if (showBanner) {
          setAnimateSaveBanner(true)
          setTimeout(() => setAnimateSaveBanner(false), 2000)
        }
      } catch (err) {}
    },
    [post, update, localArticle],
  )

  useEffect(() => {
    const keyHandler = (e: KeyboardEvent) => {
      if (e.metaKey || e.ctrlKey) {
        if (e.key === 's') {
          e.preventDefault()
          posthog.capture('dashboard:articles:edit_cmd_s:submit')
          handleSave()
        }

        if (e.key === 'p') {
          e.preventDefault()
          posthog.capture('dashboard:articles:edit_cmd_p:view')
          if (tab === 'preview') {
            setTab('edit')
          } else {
            setTab('preview')
          }
        }
      }
    }

    window.addEventListener('keydown', keyHandler)

    return () => {
      window.removeEventListener('keydown', keyHandler)
    }
  }, [handleSave, router, params, tab])

  if (!post.data) {
    return (
      <DashboardBody>
        <Spinner />
      </DashboardBody>
    )
  }

  const isPublished = Boolean(
    post.data &&
      post.data.published_at &&
      new Date(post.data.published_at) <= new Date() &&
      post.data.visibility === ArticleVisibility.PUBLIC,
  )

  const onTabChange = async (tab: string) => {
    setTab(tab)

    if (tab === 'settings') {
      handleSave(false)
      posthog.capture('dashboard:articles:edit_tab_settings:view')
    } else if (tab === 'edit') {
      posthog.capture('dashboard:articles:edit_tab_edit:view')
    } else if (tab === 'preview') {
      posthog.capture('dashboard:articles:edit_tab_preview:view')
    }
  }

  if (!post.data.organization.feature_settings?.articles_enabled) {
    return redirect(`/dashboard/${post.data.organization.slug}/posts`)
  }

  return (
    <Tabs className="flex flex-col" value={tab} onValueChange={onTabChange}>
      <div className="flex flex-row items-center gap-x-2">
        <span className="dark:text-polar-500 px-4 text-sm text-gray-500">
          {isPublished ? 'Published' : 'Unpublished'}
        </span>
        {orgContext.organization.profile_settings?.enabled && (
          <Link
            href={organizationPageLink(
              post.data.organization,
              `posts/${post.data.slug}`,
            )}
            target="_blank"
          >
            <Button variant="secondary">
              <span>Read</span>
              <ArrowUpRightIcon className="ml-2 h-3 w-3" />
            </Button>
          </Link>
        )}
        <Button
          disabled={!localHasDiff}
          onClick={() => handleSave()}
          loading={update.isPending}
        >
          Save
        </Button>
      </div>
      <PostEditor
        article={post.data}
        title={localArticle.title}
        body={localArticle.body}
        onTitleChange={(title) => setLocalArticle((a) => ({ ...a, title }))}
        onBodyChange={(body) => setLocalArticle((a) => ({ ...a, body }))}
        previewProps={{
          article: {
            ...post.data,
            title: localArticle.title,
            body: localArticle.body,
          },
          isSubscriber: true,
          hasPaidArticlesBenefit: true,
          showShare: false,
          isAuthor: true,
        }}
      />
      <AnimatePresence>
        {animateSaveBanner && (
          <motion.div
            className="fixed bottom-24 left-1/2 z-10 -translate-x-1/2"
            animate={{ opacity: 1 }}
            initial={{ opacity: 0 }}
            exit={{ opacity: 0 }}
          >
            <Banner color="default">Post was saved ✨</Banner>
          </motion.div>
        )}
      </AnimatePresence>
    </Tabs>
  )
}

export default ClientPage
