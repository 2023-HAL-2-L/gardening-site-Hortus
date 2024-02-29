$(".open-btn").click(function () {
  $(this).toggleClass('active');
  $("nav").toggleClass('nav-disable');
});
document.getElementById('image').addEventListener('change', function (event) {
  const preview = document.getElementById('imagePreview');
  const file = event.target.files[0];

  if (file) {
    const reader = new FileReader();

    reader.onload = function (e) {
      preview.src = e.target.result; // プレビュー画像のURLを設定
      preview.style.display = 'block'; // プレビュー画像を表示
    }

    reader.readAsDataURL(file);
  } else {
    preview.style.display = 'none'; // プレビュー画像を非表示
  }
});
document.addEventListener('DOMContentLoaded', function () {
  const dropArea = document.getElementById('imageUploadLabel');
  const fileInput = document.getElementById('itemImage');
  const imagePreview = document.getElementById('imagePreview');

  // ドラッグオーバー時のデフォルトの振る舞いを防止
  dropArea.addEventListener('dragover', function (e) {
    e.preventDefault();
    e.stopPropagation();
  });

  // ドロップ時の処理
  dropArea.addEventListener('drop', function (e) {
    e.preventDefault();
    e.stopPropagation();

    const files = e.dataTransfer.files;
    if (files.length > 0) {
      fileInput.files = files;

      // プレビューの表示
      const reader = new FileReader();
      reader.onload = function (e) {
        imagePreview.src = e.target.result;
        imagePreview.style.display = 'block';
      };
      reader.readAsDataURL(files[0]);
    }
  });
});

