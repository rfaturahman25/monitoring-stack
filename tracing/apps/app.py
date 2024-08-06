import opentelemetry.trace as trace
from opentelemetry.exporter.otlp.trace_exporter import OTLPTraceExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Create a tracer provider
provider = TracerProvider()
provider.add_span_processor(BatchSpanProcessor(OTLPTraceExporter(endpoint="http://jaeger:14250/api/traces")))
tracer = provider.get_tracer(__name__)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    with tracer.start_as_current_span("hello_world"):
        return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)