from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider

import logging
from random import randint
from flask import Flask, request
from flask import jsonify

# Configure Flask app
app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Setup OpenTelemetry Manual Instrumentation
provider = TracerProvider()
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

def generate_metadata():
    """ Helper function to generate trace, span """
    current_span = trace.get_current_span()

    trace_id = format(current_span.get_span_context().trace_id, "032x")
    span_id = format(current_span.get_span_context().span_id, "016x")

    metadata = {
        "trace_id": trace_id,
        "span_id": span_id,
        "http_target": request.path,
        "http_method": request.method
    }
    return metadata

def log_metadata(metadata):
    logger.info(f"Response metadata: {metadata}")

@app.route("/")
def index():
    metadata = generate_metadata()
    metadata["message"] = "Welcome to OpenTelemetry Instrumented App!"

    log_metadata(metadata)
    return jsonify(metadata)


@app.route("/home")
def manual_tracing():
    # Manually create a span
    with tracer.start_as_current_span("manual_span") as span:
        span.set_attribute("http.target", request.path)
        span.set_attribute("http.method", request.method)
        span.set_attribute("env", "development")

        # Generate metadata for manual instrumentation
        metadata = generate_metadata()
        metadata["message"] = "This is manually instrumented!"
        metadata["env"] = "Development"

        log_metadata(metadata)
        return jsonify(metadata)

@app.route("/shop")
def auto_tracing():
    metadata = generate_metadata()
    metadata["message"] = "Welcome To Our Online Shopping"

    log_metadata(metadata)
    return jsonify(metadata)

@app.route("/blog")
def metadata():
    # This endpoint shows the metadata, similar to other endpoints
    metadata = generate_metadata()
    metadata["message"] = "Welcome, Find Latest News Here!"

    log_metadata(metadata)
    return jsonify(metadata)
