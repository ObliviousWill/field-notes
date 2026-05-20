export function readingTimeMinutes(body: string | undefined, wordsPerMinute = 220): number {
	const words = (body ?? '').trim().split(/\s+/).filter(Boolean).length;
	return Math.max(1, Math.round(words / wordsPerMinute));
}
