def process_user_events(events: list[dict]) -> dict[str, int]:
    counts = {}

    for event in events:
        if not event.get("event_type") or not event.get("is_valid"):
            continue

        event_type = event["event_type"].lower().strip()
        counts[event_type] = counts.get(event_type, 0) + 1