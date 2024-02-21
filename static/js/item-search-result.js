// ページ内リンク 
$('#page-link a[href*="#"]').click(function () {
    var elmHash = $(this).attr('href'); //ページ内リンクのHTMLタグhrefから、リンクされているエリアidの値を取得
    var pos = $(elmHash).offset().top;  //idの上部の距離を取得
    $('body,html').animate({scrollTop: pos}, 500); //取得した位置にスクロール。500の数値が大きくなるほどゆっくりスクロール
    return false;
});
// ここまで

// TOPに戻るボタン
window.addEventListener('scroll',() => {
    const pageTop = document.getElementById('page-top'); //トップに戻るボタンのidを取得
    if(window.pageYOffset >= 400) {  //上から400px以上スクロールしたら
      pageTop.classList.add('fadein'); //aタグにfadeinクラスを与える
    } else {
        pageTop.classList.remove('fadein');//aタグからfadeinクラスをはずす
    }
});
// ここまで