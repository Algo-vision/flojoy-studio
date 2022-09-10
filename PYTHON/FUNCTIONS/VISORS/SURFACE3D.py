from .VCTR import fetch_inputs
from .template import init_template

def SURFACE3D(**kwargs):
    previous_job_results = fetch_inputs(kwargs['previous_job_ids'])
    payload = previous_job_results[0]

    fig = dict(
        data = [dict(
            x = list(payload['x0']),
            y = list(payload['y0']),
            z = list(payload['z0']) if 'z0' in payload else list([0] * len(payload['y0'])),
            type='surface'
        )],
        layout = dict(template = init_template())
    )
    return fig