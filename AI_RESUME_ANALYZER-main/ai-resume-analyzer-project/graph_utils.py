import matplotlib.pyplot as plt
import base64
from io import BytesIO

def generate_skill_match_graph(matched, missing):
    categories = ['Matched Skills', 'Missing Skills']
    values = [len(matched), len(missing)]

    plt.figure(figsize=(6, 4))
    bars = plt.bar(categories, values, color=['green', 'red'])
    plt.title('Skill Match Analysis')
    plt.ylabel('Number of Skills')

    # Add numbers on top
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.1, int(yval), ha='center')

    # Save to buffer
    buf = BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    # Encode as base64 string
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return img_base64

