# PM2.5 Beijing Air Quality Forecasting

A machine learning project using RNN/LSTM models to forecast PM2.5 air pollution levels in Beijing.

## 🎯 Project Goals
- Achieve RMSE < 4000 for PM2.5 forecasting
- Compare LSTM vs GRU performance
- Provide real-time air quality predictions

## 📊 Dataset
Place your dataset files in `data/raw/`:
- `beijing_pm25.csv` - Historical PM2.5 measurements
- `weather_data.csv` - Weather data (temperature, humidity, wind, pressure)

## 🚀 Quick Start
```bash
# Clone repository
git clone https://github.com/yourusername/pm25-beijing-forecasting-rnn.git
cd pm25-beijing-forecasting-rnn

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the forecasting model
python src/pm25_forecaster.py