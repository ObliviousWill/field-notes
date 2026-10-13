import { defineCollection, reference } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const blog = defineCollection({
	loader: glob({ base: './src/content/blog', pattern: '**/*.{md,mdx}' }),
	schema: ({ image }) =>
		z.object({
			title: z.string(),
			description: z.string(),
			pubDate: z.coerce.date(),
			updatedDate: z.coerce.date().optional(),
			heroImage: z.optional(image()),
			tags: z.array(z.enum(['building', 'marketing', 'ai'])).optional(),
			author: z.string().optional(),
			mentions: z.array(reference('projects')).optional(),
			// site-relative path to a recording of the post, e.g. /blog/audio/my-post.mp3
			audio: z.string().startsWith('/').optional(),
		}),
});

const projects = defineCollection({
	loader: glob({ base: './src/content/projects', pattern: '**/*.{md,mdx}' }),
	schema: ({ image }) =>
		z.object({
			title: z.string(),
			summary: z.string(),
			status: z.enum(['building', 'shipped', 'paused']),
			// who it's for: drives the grouping on the projects page
			area: z.enum(['work', 'local', 'personal']).default('personal'),
			startDate: z.coerce.date(),
			heroImage: z.optional(image()),
			links: z
				.array(
					z.object({
						label: z.string(),
						// absolute for anything off-site, or a site-relative path like /pista/
						url: z.union([z.string().url(), z.string().startsWith('/')]),
					}),
				)
				.optional(),
			facts: z
				.array(
					z.object({
						label: z.string(),
						value: z.string(),
					}),
				)
				.optional(),
		}),
});

const updates = defineCollection({
	loader: glob({ base: './src/content/updates', pattern: '**/*.{md,mdx}' }),
	schema: ({ image }) =>
		z.object({
			project: reference('projects'),
			title: z.string(),
			pubDate: z.coerce.date(),
			image: z.optional(image()),
		}),
});

const guides = defineCollection({
	loader: glob({ base: './src/content/guides', pattern: '**/*.{md,mdx}' }),
	schema: z.object({
		title: z.string(),
		description: z.string(),
		pubDate: z.coerce.date(),
		updatedDate: z.coerce.date().optional(),
		// position in the reading order on /guides/
		step: z.number().int().positive(),
		audio: z.string().startsWith('/').optional(),
	}),
});

export const collections = { blog, projects, updates, guides };
