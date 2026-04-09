import os
import json

def handler(request):
    """Vercel serverless function handler"""
    try:
        # Get path from request
        path = request.get('path', '/')

        if path == '/api/health':
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({
                    'status': 'healthy',
                    'service': 'SMS Backend',
                    'message': 'Basic Vercel function working'
                })
            }
        elif path == '/api/send-sms':
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({
                    'success': False,
                    'message': 'SMS functionality not yet implemented'
                })
            }
        else:
            return {
                'statusCode': 404,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'Not found'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)})
        }
