import { getCollection, type CollectionEntry } from 'astro:content';
import type { APIContext } from 'astro';
import { generateOgPng } from '../../../utils/og';

export async function getStaticPaths() {
	const guides = await getCollection('guides');
	return guides.map((guide) => ({ params: { slug: guide.id }, props: { guide } }));
}

interface Props {
	guide: CollectionEntry<'guides'>;
}

export async function GET({ props }: APIContext<Props>) {
	const { guide } = props;
	const png = await generateOgPng({
		title: guide.data.title,
		description: guide.data.description,
		meta: `Guide ${guide.data.step}  ·  Getting started with Claude`,
		eyebrow: 'FIELD NOTES',
	});
	return new Response(png, { headers: { 'Content-Type': 'image/png' } });
}
