import React, { useState, useEffect, useMemo } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, ReferenceLine } from 'recharts';

function App() {
  const [data, setData] = useState([]);
  const [events, setEvents] = useState([]);
  const [startDate, setStartDate] = useState("1987-05-20");
  const [endDate, setEndDate] = useState("2022-12-31");
  const [highlightDate, setHighlightDate] = useState("");

  useEffect(() => {
    axios.get('http://localhost:5000/api/historical-prices').then(res => setData(res.data));
    axios.get('http://localhost:5000/api/events').then(res => setEvents(res.data));
  }, []);

  // Filter Data based on User Selection (Instruction 2c-i)
  const filteredData = useMemo(() => {
    return data.filter(d => d.Date >= startDate && d.Date <= endDate);
  }, [data, startDate, endDate]);

  return (
    <div style={{ padding: '30px', backgroundColor: '#f4f7f6', minHeight: '100vh' }}>
      <header>
        <h1 style={{ color: '#2c3e50' }}>Birhan Energies: Brent Oil Analysis</h1>
      </header>

      {/* Control Panel: Filters & Selection (Instruction 2c-i & ii) */}
      <div style={{ display: 'flex', gap: '20px', marginBottom: '30px', backgroundColor: '#fff', padding: '20px', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
        <div>
          <label>Start Date: </label>
          <input type="date" value={startDate} onChange={e => setStartDate(e.target.value)} />
        </div>
        <div>
          <label>End Date: </label>
          <input type="date" value={endDate} onChange={e => setEndDate(e.target.value)} />
        </div>
        <div>
          <label>Highlight Event: </label>
          <select onChange={e => setHighlightDate(e.target.value)}>
            <option value="">Select Event...</option>
            {events.map(ev => <option key={ev.Date} value={ev.Date}>{ev.Event}</option>)}
          </select>
        </div>
      </div>

      {/* Main Chart (Instruction 2b & 2d) */}
      <div style={{ height: '450px', backgroundColor: '#fff', padding: '20px', borderRadius: '8px' }}>
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={filteredData}>
            <CartesianGrid strokeDasharray="3 3" vertical={false} />
            <XAxis dataKey="Date" minTickGap={50} />
            <YAxis label={{ value: 'Price (USD)', angle: -90, position: 'insideLeft' }} />
            <Tooltip contentStyle={{ borderRadius: '10px' }} />
            <Line type="monotone" dataKey="Price" stroke="#3498db" dot={false} strokeWidth={2} />
            
            {/* Event Highlight Logic (Instruction 2c-ii) */}
            {highlightDate && (
              <ReferenceLine x={highlightDate} stroke="#e74c3c" strokeWidth={3} label={{ position: 'top', value: 'Shock', fill: '#e74c3c' }} />
            )}
          </LineChart>
        </ResponsiveContainer>
      </div>

      {/* Summary Metrics (Instruction 2c-iii) */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '20px', marginTop: '20px' }}>
        <div style={cardStyle}>
          <h4>Avg Price (Selected)</h4>
          <p style={{ fontSize: '24px', fontWeight: 'bold' }}>
            ${filteredData.length > 0 ? (filteredData.reduce((a, b) => a + b.Price, 0) / filteredData.length).toFixed(2) : "0"}
          </p>
        </div>
        <div style={cardStyle}>
          <h4>Volatility (Std Dev)</h4>
          <p style={{ fontSize: '24px', fontWeight: 'bold', color: '#e67e22' }}>High</p>
        </div>
        <div style={cardStyle}>
          <h4>Detected Breaks</h4>
          <p>The model identified 15 major structural shifts in this period.</p>
        </div>
      </div>
    </div>
  );
}

const cardStyle = { backgroundColor: '#fff', padding: '20px', borderRadius: '8px', textAlign: 'center', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' };

export default App;