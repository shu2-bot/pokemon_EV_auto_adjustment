//インデント番号を設定
let i = 2
function addForm() {
    // 8人以上なら処理を終了する
    if (i > 8) {
        return true;

    } else {
        // 複製するHTML要素を取得
        const element = document.getElementById("opposite_pokemon_1");

        // 要素を複製
        const newelement = element.cloneNode(true);

        // 子要素を指定しname属性の値を変更
        const newelement_name = newelement.children[0];
        newelement_name.name = 'name-'+i;
//
        //const newelement_age = newelement.children[1];
        //newelement_age.name = 'age-'+i;

        //親要素を取得し 複製した要素を追加
        const parent = document.getElementById("input_pokemon_form");
        parent.appendChild(newelement);

       //インデント番号を更新
        i++;
    }
}