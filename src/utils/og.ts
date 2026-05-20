import fs from 'node:fs/promises';
import path from 'node:path';
import { Resvg } from '@resvg/resvg-js';
import satori from 'satori';

let fontCache: { regular: Buffer; bold: Buffer } | null = null;

async function loadFonts() {
	if (fontCache) return fontCache;
	const regular = await fs.readFile(path.resolve('src/assets/fonts/atkinson-regular.woff'));
	const bold = await fs.readFile(path.resolve('src/assets/fonts/atkinson-bold.woff'));
	fontCache = { regular, bold };
	return fontCache;
}

interface OgOptions {
	title: string;
	description?: string;
	meta?: string;
	eyebrow?: string;
}

const BG = '#EEE9DF';
const TEXT = '#2C3B4D';
const TEXT_MUTED = '#4F5D6F';
const ACCENT = '#FFB162';

interface SatoriNode {
	type: string;
	props: {
		style?: Record<string, unknown>;
		children?: SatoriChildren;
	};
}
type SatoriChildren = string | SatoriNode | Array<SatoriNode | string>;

function el(
	type: string,
	style: Record<string, unknown>,
	children: SatoriChildren = '',
): SatoriNode {
	return { type, props: { style, children } };
}

export async function generateOgPng(options: OgOptions): Promise<Buffer> {
	const { regular, bold } = await loadFonts();

	const children: SatoriNode[] = [
		el(
			'div',
			{
				fontSize: 28,
				color: TEXT_MUTED,
				textTransform: 'uppercase',
				letterSpacing: 4,
				fontWeight: 700,
				marginBottom: 30,
			},
			options.eyebrow ?? 'FIELD NOTES',
		),
		el(
			'div',
			{
				fontSize: 72,
				fontWeight: 700,
				lineHeight: 1.1,
				color: TEXT,
				maxWidth: 1040,
				marginBottom: 40,
				display: 'flex',
			},
			options.title,
		),
	];

	if (options.description) {
		children.push(
			el(
				'div',
				{
					fontSize: 30,
					color: TEXT_MUTED,
					lineHeight: 1.35,
					maxWidth: 1040,
					fontStyle: 'italic',
					display: 'flex',
				},
				options.description,
			),
		);
	}

	children.push(el('div', { flex: 1, display: 'flex' }));

	children.push(
		el(
			'div',
			{
				display: 'flex',
				alignItems: 'center',
				fontSize: 24,
				color: TEXT_MUTED,
			},
			[
				el('div', {
					width: 14,
					height: 14,
					backgroundColor: ACCENT,
					borderRadius: 7,
					marginRight: 14,
				}),
				options.meta ?? '',
			],
		),
	);

	const root = el(
		'div',
		{
			width: '100%',
			height: '100%',
			display: 'flex',
			flexDirection: 'column',
			backgroundColor: BG,
			padding: 80,
			fontFamily: 'Atkinson',
			color: TEXT,
		},
		children,
	);

	// eslint-disable-next-line @typescript-eslint/no-explicit-any
	const svg = await satori(root as any, {
		width: 1200,
		height: 630,
		fonts: [
			{ name: 'Atkinson', data: regular, weight: 400, style: 'normal' },
			{ name: 'Atkinson', data: bold, weight: 700, style: 'normal' },
		],
	});

	const resvg = new Resvg(svg, { fitTo: { mode: 'width', value: 1200 } });
	return resvg.render().asPng();
}
