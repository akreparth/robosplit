from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_splits(original_total, train_pct, val_pct, test_pct, multiplier):
    # Validate percentages
    if train_pct + val_pct + test_pct != 100:
        return None, "Error: Percentages must sum to 100"
    
    try:
        # Calculate initial training size
        denominator = (100 * multiplier) - (multiplier - 1) * train_pct
        train_initial = (train_pct * original_total) / denominator
        train_initial = round(train_initial)
        
        # Calculate total after augmentation
        total_after_aug = multiplier * train_initial + (original_total - train_initial)
        
        # Calculate validation and test
        val_initial = round((val_pct / 100) * total_after_aug)
        test_initial = round((test_pct / 100) * total_after_aug)
        
        # Adjust for rounding errors
        required_sum = original_total - train_initial
        if val_initial + test_initial != required_sum:
            test_initial = required_sum - val_initial
        
        return {
            'original_total': original_total,
            'multiplier': multiplier,
            'initial_split': (train_initial, val_initial, test_initial),
            'augmented_split': (multiplier * train_initial, val_initial, test_initial),
            'total_after_aug': total_after_aug
        }, None
    
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
            multiplier = int(request.form['multiplier'])
            
            # Validate multiplier
            if not (2 <= multiplier <= 50):
                return render_template('index.html', error="Multiplier must be between 2-50")
            
            results, error = calculate_splits(original_total, train_pct, val_pct, test_pct, multiplier)
            
            if error:
                return render_template('index.html', error=error)
            
            return render_template('result.html', results=results)
        
        except ValueError:
            return render_template('index.html', error="Invalid input values")
    
    # Default values for GET request
    return render_template('index.html')