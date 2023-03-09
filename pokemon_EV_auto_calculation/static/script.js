//インデント番号を設定
let i = 2
function addForm() {
    // 8人以上なら処理を終了する
    if (i > 8) {
        return true;

    } else {
        // 複製するHTML要素を取得
        const element = document.getElementById("opposite_pokemon");

        // 要素を複製
        const newelement = element.cloneNode(true);
        //newelement.getElementById('id_speed').innerHTML;

        //let len = newelement.children.length;
        //console.log("ノード数:" + len);
        //console.log("ノード数:" + newelement.children[0].innerText);
        //console.log("ノード数:" + newelement.children[4].innerText);
        //console.log("ノード数:" + newelement.children[9]);
        //console.log("ノード数:" + newelement.children[11].innerText);

        let len2 = newelement.childNodes.length;
        console.log(len2);
        console.log(newelement.childNodes[16])
        console.log(newelement.childNodes[17])
        console.log(newelement.childNodes[18])
        console.log(newelement.childNodes[19])
        console.log(newelement.childNodes[19].nodeName)

        // 子要素を指定しname属性の値を変更
        //const newelement_name1 = newelement.children[2];
        //newelement_name.name = 'value'+i;
        //newelement_name1.name = "hogehoge";

        // 子要素を指定しname属性の値を変更
        const newelement_name = newelement.childNodes[19];
        //newelement_name.name = 'value'+i;
        newelement_name.value = i;
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

function tab_close() {
    //できないみたい
    window.close();
}