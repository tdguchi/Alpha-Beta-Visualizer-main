#!/usr/bin/env python3
"""
Alpha-Beta Visualizer Flask Application

A Flask web application for visualizing the Alpha-Beta pruning algorithm
in minimax trees. This interactive tool allows users to create, modify,
and step through the algorithm execution.
"""

from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Configuration
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    """
    Main route that serves the Alpha-Beta Visualizer interface.
    
    Returns:
        Rendered HTML template for the main application interface.
    """
    return render_template('index.html')

@app.route('/health')
def health():
    """
    Health check endpoint for monitoring and load balancers.
    
    Returns:
        JSON response with health status.
    """
    return {
        'status': 'healthy',
        'service': 'alpha-beta-visualizer',
        'version': '1.0.0'
    }, 200

@app.route('/favicon.ico')
def favicon():
    """
    Serve the favicon from the static images directory.
    
    Returns:
        Static favicon file.
    """
    return send_from_directory(
        os.path.join(app.root_path, 'static', 'images'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors by redirecting to the main page.
    
    Args:
        error: The 404 error object.
        
    Returns:
        Redirect to the main application interface.
    """
    return render_template('index.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors gracefully.
    
    Args:
        error: The 500 error object.
        
    Returns:
        JSON error response or redirect to main page.
    """
    return render_template('index.html'), 500

if __name__ == '__main__':
    # Ensure the application runs in debug mode for development
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        threaded=True
    )
