
def simulate_pipeline(pipeline_name):
    """Simulate Jenkins pipeline execution"""
    print(f"Running Jenkins pipeline: {pipeline_name}")
    return {"status": "success", "pipeline": pipeline_name}
