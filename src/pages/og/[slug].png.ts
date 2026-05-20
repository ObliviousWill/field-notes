import { getCollection, type CollectionEntry } from 'astro:content';
import type { APIContext } from 'astro';
import { generateOgPng } from '../../utils/og';
import { readingTimeMinutes } from '../../utils/readingTime';

export async function getStaticPaths() {
	const posts = await getCollection('blog');
	return posts.map((post) => ({ params: { slug: post.id }, props: { post } }));
}

interface Props {
	post: CollectionEntry<'blog'>;
}

export async function GET({ props }: APIContext<Props>) {
	const { post } = props;
	const date = post.data.pubDate.toLocaleDateString('en-GB', {
		year: 'numeric',
		month: 'long',
		day: 'numeric',
	});
	const readingTime = readingTimeMinutes(post.body);
	const png = await generateOgPng({
		title: post.data.title,
		description: post.data.description,
		meta: `${date}  ·  ${readingTime} min read`,
		eyebrow: 'FIELD NOTES',
	});
	return new Response(png, { headers: { 'Content-Type': 'image/png' } });
}
