from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_splits(original_total, train_pct, val_pct, test_pct):
    # Validation
    if train_pct + val_pct + test_pct != 100:
        return None, "Error: Percentages must sum to 100"
    
    try:
        # Calculations
        train_initial = (train_pct * original_total) / (300 - 2 * train_pct)
        train_initial = round(train_initial)
        
        total_after_aug = 3 * train_initial + (original_total - train_initial)
        
        val_initial = round((val_pct / 100) * total_after_aug)
        test_initial = round((test_pct / 100) * total_after_aug)
        
        # Adjust for rounding
        required_sum = original_total - train_initial
        if val_initial + test_initial != required_sum:
            test_initial = required_sum - val_initial
        
        # Prepare results
        results = {
            'original_total': original_total,
            'initial_split': (train_initial, val_initial, test_initial),
            'augmented_split': (3 * train_initial, val_initial, test_initial),
            'total_after_aug': total_after_aug
        }
        return results, None
    
    except Exception as e:
        return None, f"Calculation error: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            original_total = int(request.form['total'])
            train_pct = float(request.form['train'])
            val_pct = float(request.form['val'])
            test_pct = float(request.form['test'])
            
            results, error = calculate_splits(original_total, train_pct, val_pct, test_pct)
            
            if error:
                return render_template('index.html', error=error)
            
            return render_template('result.html', results=results)
        
        except ValueError:
            return render_template('index.html', error="Invalid input values")
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)