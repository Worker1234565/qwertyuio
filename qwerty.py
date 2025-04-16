from flask import Flask, request, render_template_string
import datetime

app = Flask(__name__)

# Список для хранения IP-адресов и времени посещения
visitors = []

# HTML-шаблон для отображения IP-адресов
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IP Tracker</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #333; }
        table { border-collapse: collapse; width: 100%; max-width: 600px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Your IP Address: {{ current_ip }}</h1>
    <h2>Visitors</h2>
    <table>
        <tr>
            <th>IP Address</th>
            <th>Time (UTC)</th>
        </tr>
        {% for visitor in visitors %}
        <tr>
            <td>{{ visitor['ip'] }}</td>
            <td>{{ visitor['time'] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route('/')
def track_ip():
    # Получаем IP-адрес посетителя
    visitor_ip = request.remote_addr
    # Получаем текущее время в UTC
    visit_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    
    # Добавляем информацию о посетителе в список
    visitors.append({'ip': visitor_ip, 'time': visit_time})
    
    # Рендерим шаблон с данными
    return render_template_string(HTML_TEMPLATE, current_ip=visitor_ip, visitors=visitors)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
