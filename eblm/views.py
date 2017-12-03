"""
Views for flask-eblm project
"""
from datetime import datetime
from functools import (
    wraps,
    update_wrapper
    )
from flask import (
    render_template,
    make_response
    )
from eblm.db import (
    getAllEblmParameters,
    getAllStellarParameters
    )
from eblm import app

def nocache(view):
    """
    Wrapper to stop caching
    """
    @wraps(view)
    def no_cache(*args, **kwargs):
        """
        Function to stop caching
        """
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
    return update_wrapper(no_cache, view)

@app.route('/')
@nocache
def eblm_index():
    """
    Rander the main summary page
    """
    eblms = getAllEblmParameters()
    return render_template('index.html', eblms=eblms)

@app.route('/stellar_parameters')
@nocache
def stellar_parameters():
    """
    Rander the stellar parameters page
    """
    params = getAllStellarParameters()
    return render_template('stellar_parameters.html', params=params)
