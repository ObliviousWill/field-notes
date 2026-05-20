import { generateOgPng } from '../../utils/og';

export async function GET() {
	const png = await generateOgPng({
		title: 'Field Notes',
		description:
			'Notes from the field on marketing, building, and AI in practice — by Will.',
		meta: 'fieldnotes by Will',
		eyebrow: 'FIELD NOTES',
	});
	return new Response(png, { headers: { 'Content-Type': 'image/png' } });
}
