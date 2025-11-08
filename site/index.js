// Имитация данных пользователя из Telegram
document.addEventListener('DOMContentLoaded', function() {
    // В реальном приложении эти данные будут приходить из Telegram Mini Apps
    const userData = {
        id: 123456789,
        firstName: "Иван",
        lastName: "Петров",
        username: "ivan_petrov",
        photoUrl: "https://via.placeholder.com/100/0088cc/ffffff?text=IP"
    };
    
    // Заполняем данные профиля
    document.getElementById('user-name').textContent = `${userData.firstName} ${userData.lastName}`;
    document.getElementById('user-username').textContent = `@${userData.username}`;
    document.getElementById('user-avatar').src = userData.photoUrl;
    
    // Имитация статистики (в реальном приложении данные будут из базы)
    const stats = {
        completedTasks: 42,
        successRate: 85,
        rating: 4.7
    };
    
    document.getElementById('completed-tasks').textContent = stats.completedTasks;
    document.getElementById('success-rate').textContent = `${stats.successRate}%`;
    document.getElementById('rating').textContent = stats.rating;
    
    // Обработчик переключения темы
    const themeToggle = document.getElementById('theme-toggle');
    
    // Проверяем сохраненную тему
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-theme');
        themeToggle.checked = true;
    }
    
    themeToggle.addEventListener('change', function() {
        if (this.checked) {
            document.body.classList.add('dark-theme');
            localStorage.setItem('theme', 'dark');
        } else {
            document.body.classList.remove('dark-theme');
            localStorage.setItem('theme', 'light');
        }
    });
});