import rss from '@astrojs/rss';
import { SITE_TITLE } from '../../consts';
import { getAllUpdates, updateSlug } from '../../utils/projects';

const base = import.meta.env.BASE_URL.replace(/\/$/, '');

export async function GET(context) {
	const updates = await getAllUpdates();
	return rss({
		title: `${SITE_TITLE} — Project updates`,
		description: 'Progress updates from projects on Field Notes.',
		site: context.site,
		items: updates.map((update) => ({
			title: update.data.title,
			pubDate: update.data.pubDate,
			link: `${base}/projects/${update.data.project.id}/${updateSlug(update)}/`,
		})),
	});
}
