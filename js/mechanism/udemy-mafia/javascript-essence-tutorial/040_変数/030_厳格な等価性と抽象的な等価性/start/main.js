// 厳格な等価性→型の比較までする
// 抽象的な等価性→型の比較なし→まぁイメージとして暗黙的な型変換が実行された後に厳格比較する感じ、そりゃ型の等価はしていないよねってことだ、比較ではないかな？

// 厳格な等価性比較は===でできる以下例
const a = 1;
const b = "1";
console.log(a === b); // false
console.log(a == b); // true　型変換して合わせてくれるというね

// 子のトピックに関しては、ECMScriptに仕様が詳細にあるので要チェック、truthy,falsyにも注意ね