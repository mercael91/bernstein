const ACK_MARKER = /<!--[ \t]*bot-ack:[^\r\n]*-->/g;

/** Preserve acknowledgement markers when the review bot regenerates a PR body. */
export function preserveAckMarkers(previousBody: string, regeneratedBody: string): string {
  const previousMarkers = previousBody.match(ACK_MARKER) ?? [];
  const currentMarkers = new Set(regeneratedBody.match(ACK_MARKER) ?? []);
  const missingMarkers = previousMarkers.filter((marker) => !currentMarkers.has(marker));

  if (missingMarkers.length === 0) {
    return regeneratedBody;
  }

  return `${regeneratedBody.trimEnd()}\n\n${missingMarkers.join("\n")}\n`;
}
