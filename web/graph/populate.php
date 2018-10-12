<pre><?php
$root = "https://github.com/sarahscheffler/mapofcrypto/tree/master/";

$c = curl_init();
curl_setopt($c, CURLOPT_URL, "$root/objects/Edges/");
curl_setopt($c, CURLOPT_RETURNTRANSFER, 1);
$html = curl_exec($c);
curl_close($c);
$dom = new DOMDocument();
@$dom->loadHTML($html);
foreach($dom->getElementsByTagName('a') as $a) {  //or class=js-navigation-open
        $a = $a->getAttribute('href');
        if(substr($a, -5) === '.json'){
            $a = str_replace("blob/", "", $a);
            $json["edge"][] = "https://raw.githubusercontent.com$a";
        }
}

$c = curl_init();
curl_setopt($c, CURLOPT_URL, "$root/objects/Nodes/");
curl_setopt($c, CURLOPT_RETURNTRANSFER, 1);
$html = curl_exec($c);
curl_close($c);
$dom = new DOMDocument();
@$dom->loadHTML($html);
foreach($dom->getElementsByTagName('a') as $a) {
        $a = $a->getAttribute('href');
        if(substr($a, -5) === '.json'){
            $a = str_replace("blob/", "", $a);
            $json["node"][] = "https://raw.githubusercontent.com$a";
        }
}

$nodes = array();
foreach ($json["node"] as $k) {
    $node = json_decode(file_get_contents("$k"), true);
    $nodes[$node["uid"]] = $node;
}

foreach ($json["edge"] as $k) {
    $node = json_decode(file_get_contents("$k"), true);
    $json["links"][] = array(
        "source" => $nodes[$node["source_nodes"][0]]["display_name"],
        "target" => $nodes[$node["dest_node"]]["display_name"],
        "color" => mt_rand(0,7)
    );
}
$links = json_encode($json["links"], JSON_PRETTY_PRINT);
echo($links);
file_put_contents("links.txt", $links);


foreach ($json["node"] as $k) {
    $node = json_decode(file_get_contents("$k"), true);
    $json["primitives"][] = array(
        "source" => $node["display_name"],
        "textsize" => 18,
        "color" => mt_rand(0,7)
    );
}
$primitives = json_encode($json["primitives"], JSON_PRETTY_PRINT);
echo($primitives);
file_put_contents("primitives.txt", $links);


foreach ($json["node"] as $k) {
    $node = json_decode(file_get_contents("$k"), true);
    $json["info"][$node["display_name"]] = $node;
}
$info = json_encode($json["info"], JSON_PRETTY_PRINT);
echo($info);
file_put_contents("info.txt", $links);
?>
