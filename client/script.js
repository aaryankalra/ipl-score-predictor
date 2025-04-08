const teams = [
    'Mumbai Indians', 'Chennai Super Kings', 'Royal Challengers Bangalore', 'Kolkata Knight Riders',
    'Rajasthan Royals', 'Kings XI Punjab', 'Sunrisers Hyderabad', 'Delhi Daredevils',
    'Delhi Capitals', 'Deccan Chargers', 'Punjab Kings', 'Lucknow Super Giants',
    'Gujarat Titans', 'Pune Warriors', 'Gujarat Lions', 'Royal Challengers Bengaluru',
    'Rising Pune Supergiant', 'Kochi Tuskers Kerala', 'Rising Pune Supergiants'
];

const cities = [
    'Mumbai', 'Kolkata', 'Delhi', 'Chennai', 'Hyderabad', 'Bangalore', 'Chandigarh', 'Jaipur',
    'Pune', 'Dubai', 'Abu Dhabi', 'Ahmedabad', 'Bengaluru', 'Sharjah', 'Visakhapatnam',
    'Durban', 'Lucknow', 'Dharamsala', 'Centurion', 'Rajkot', 'Navi Mumbai', 'Indore',
    'Johannesburg', 'Port Elizabeth', 'Cuttack', 'Ranchi', 'Cape Town', 'Raipur',
    'Mohali', 'Kochi'
];

function populateDropdown(id, values) {
    const select = document.getElementById(id);
    values.sort().forEach(value => {
        const option = document.createElement("option");
        option.value = value;
        option.text = value;
        select.add(option);
    });
}

populateDropdown("batting_team", teams);
populateDropdown("bowling_team", teams);
populateDropdown("city", cities);

async function predict() {
    const data = {
        batting_team: document.getElementById("batting_team").value,
        bowling_team: document.getElementById("bowling_team").value,
        city: document.getElementById("city").value,
        current_score: parseInt(document.getElementById("current_score").value),
        overs_done: parseFloat(document.getElementById("overs_done").value),
        wickets_down: parseInt(document.getElementById("wickets_down").value),
        last_five: parseInt(document.getElementById("last_five").value)
    };

    const response = await fetch("http://localhost:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    document.getElementById("result").innerText = "Predicted Final Score: " + result.predicted_score;
}