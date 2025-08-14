package it.ns.mcp_server;

import org.springframework.ai.tool.annotation.Tool;
import org.springframework.ai.tool.annotation.ToolParam;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class TrackingService {

    @Tool(description = "Get the tracking events for a specific shipment identified by the shipment number")
    public List<TrackingEvent> getTrackingEventsForShipment(@ToolParam(description = "14 digit shipment number") String shipmentNumber ) {
        return TrackingEvent.generateMockEvents();
    }

}
