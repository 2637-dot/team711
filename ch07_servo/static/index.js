const input = document.getElementById('number');
const button = document.getElementById('submitBtn');

button.addEventListener('click', function(event) {
    event.preventDefault();

    const angleValue = input.value;

    if (angleValue === '') {
        alert('각도를 입력해 주세요!');
        return;
    }

    fetch('/api/angle', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ angle: angleValue })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error('Error:', error);
        alert('서버와 통신 중 오류가 발생했습니다.');
    });
});
