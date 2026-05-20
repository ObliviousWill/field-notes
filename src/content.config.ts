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
		}),
});

const projects = defineCollection({
	loader: glob({ base: './src/content/projects', pattern: '**/*.{md,mdx}' }),
	schema: ({ image }) =>
		z.object({
			title: z.string(),
			summary: z.string(),
			status: z.enum(['building', 'shipped', 'paused']),
			startDate: z.coerce.date(),
			heroImage: z.optional(image()),
			links: z
				.array(
					z.object({
						label: z.string(),
						url: z.string().url(),
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

export const collections = { blog, projects, updates };
