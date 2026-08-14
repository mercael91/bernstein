function regenerateBody(prBody) {
  const markers = prBody.match(/<!-- bot-ack: <id> reason=... -->/g);
  if (markers) {
    prBody += markers.join('');
  }
  return prBody;
}