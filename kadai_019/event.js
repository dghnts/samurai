// ボタン要素を取得
const btn = document.getElementById("btn");

// h2要素を取得
const text = document.getElementById("text");

// ボタンをクリックしたときにイベントが発生するようにする
btn.addEventListener('click', () => {
    text.textContent = "ボタンをクリックしました"
});