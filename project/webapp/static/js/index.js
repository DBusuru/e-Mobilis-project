document.querySelector('form').addEventListener('submit', function (e) {
  const password = document.querySelector('input[type="password"]:nth-child(3)').value;
  const confirmPassword = document.querySelector('input[type="password"]:nth-child(4)').value;

  if (password !== confirmPassword) {
    e.preventDefault();
    alert('Passwords do not match!');
  }
});
