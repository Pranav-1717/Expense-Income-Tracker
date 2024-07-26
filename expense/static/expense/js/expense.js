document.addEventListener('DOMContentLoaded', function() {
    getMonthlyCategoryChartData();
});

const getColorMapping = (categories) => {
    const colors = [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 159, 64, 0.2)',
        'rgba(99, 255, 132, 0.2)',
        'rgba(235, 162, 54, 0.2)',
        'rgba(206, 255, 86, 0.2)',
        'rgba(192, 75, 192, 0.2)',
        'rgba(102, 153, 255, 0.2)',
        'rgba(159, 255, 64, 0.2)'
    ];
    const borderColors = [
        'rgba(255, 99, 132, 1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)',
        'rgba(99, 255, 132, 1)',
        'rgba(235, 162, 54, 1)',
        'rgba(206, 255, 86, 1)',
        'rgba(192, 75, 192, 1)',
        'rgba(102, 153, 255, 1)',
        'rgba(159, 255, 64, 1)'
    ];

    let colorMapping = {};
    categories.forEach((category, index) => {
        colorMapping[category] = {
            backgroundColor: colors[index % colors.length],
            borderColor: borderColors[index % borderColors.length]
        };
    });

    return colorMapping;
}

const renderStackedBarChart = (data, labels, categories) => {
    const ctx = document.getElementById('monthlyCategoryExpensesChart').getContext('2d');
    const colorMapping = getColorMapping(categories);

    const datasets = categories.map((category) => {
        return {
            label: category,
            data: labels.map(month => data[month][category] || 0),
            backgroundColor: colorMapping[category].backgroundColor,
            borderColor: colorMapping[category].borderColor,
            borderWidth: 1
        };
    });

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: datasets
        },
        options: {
            scales: {
                x: {
                    stacked: true
                },
                y: {
                    stacked: true,
                    beginAtZero: true
                }
            },
            plugins: {
                title: {
                    display: true,
                    text: 'Monthly Category-wise Expenses'
                }
            }
        }
    });
};

const getMonthlyCategoryChartData = () => {
    fetch("/expense_monthly_category_summary/")
        .then((res) => res.json())
        .then((results) => {
            console.log("results", results);
            const monthlyData = results.monthly_data;
            const labels = Object.keys(monthlyData).sort();
            const categories = new Set();

            labels.forEach(month => {
                Object.keys(monthlyData[month]).forEach(category => categories.add(category));
            });

            renderStackedBarChart(monthlyData, labels, Array.from(categories));
        })
        .catch((error) => {
            console.error('Error fetching data:', error);
        });
};
