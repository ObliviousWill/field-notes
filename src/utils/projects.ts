import { getCollection, type CollectionEntry } from 'astro:content';

export type Project = CollectionEntry<'projects'>;
export type Update = CollectionEntry<'updates'>;

export async function getUpdatesForProject(projectId: string): Promise<Update[]> {
	const updates = await getCollection('updates');
	return updates
		.filter((u) => u.data.project.id === projectId)
		.sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
}

export async function getAllUpdates(): Promise<Update[]> {
	const updates = await getCollection('updates');
	return updates.sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
}

export function updateSlug(update: Update): string {
	const parts = update.id.split('/');
	return parts[parts.length - 1] ?? update.id;
}

export function updatePath(update: Update, base: string): string {
	return `${base}/projects/${update.data.project.id}/${updateSlug(update)}/`;
}
