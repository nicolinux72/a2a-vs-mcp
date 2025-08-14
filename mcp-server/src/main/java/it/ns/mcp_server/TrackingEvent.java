package it.ns.mcp_server;

import java.time.LocalDateTime;
import java.util.List;

public record TrackingEvent(
    LocalDateTime timestamp,
    String depot,
    Event event
) {
    public static List<TrackingEvent> generateMockEvents() {
        LocalDateTime t0 = LocalDateTime.now().minusDays(2);
        return List.of(
                new TrackingEvent(t0, "Bologna", Event.IN_DEPOT),
                new TrackingEvent(t0.plusHours(2), "Bologna", Event.SHIPPED),
                new TrackingEvent(t0.plusHours(18), "Lione", Event.IN_DEPOT),
                new TrackingEvent(t0.plusHours(30), "Parigi", Event.IN_DEPOT),
                new TrackingEvent(t0.plusHours(36), "Parigi", Event.DELIVERY),
                new TrackingEvent(t0.plusHours(40), "Parigi", Event.DELIVERED)
        );
    }
}
