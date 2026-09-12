from pathlib import Path
import requests

out = Path(r"E:\trip\images\steps")
out.mkdir(parents=True, exist_ok=True)
items = {
    "hgh-t4.jpg": "https://commons.wikimedia.org/wiki/Special:FilePath/202403%20Airside%20Lobby%20of%20HGH%20T4%20International%20Departure%20(1).jpg",
    "china-southern.jpg": "https://cdn.plnspttrs.net/22971/b-1293-china-southern-airlines-boeing-787-9-dreamliner_PlanespottersNet_1057913_be420cb08d_o.jpg",
    "schiphol.jpg": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2018/12/31/18/schiphol-airport-amsterdam.jpg",
    "amsterdam-centraal.jpg": "https://commons.wikimedia.org/wiki/Special:FilePath/Amsterdam%20Centraal%20front.jpg",
    "rijksmuseum.jpg": "https://www.jarvisen.com/cdn/shop/articles/Amsterdam_-_Rijksmuseum.jpg?v=1611689049",
    "amsterdam-canal.jpg": "https://www.rederijkooij.nl/sites/default/files/styles/max_1300x1300/public/2020-12/kennedy_02.jpeg?itok=LH-Naoaw",
    "eurostar-amsterdam.jpg": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Eurostar_te_station_Amsterdam_Centraal_%282%29.jpg",
    "guerrisol.jpg": "https://i.pinimg.com/736x/85/3f/cd/853fcd82d56e42a93eb71d1217055362.jpg",
    "freepstar.jpg": "https://www.lovehappensmag.com/blog/wp-content/uploads/2018/09/Free-P-Star-Vintage-shopping-in-Le-Marais-Paris-Source-Parisperfect.jpg",
    "rue-rosiers.webp": "https://static.liontech.com.tw/DS/go_images/1/3948/3949/3950/Q3176233/Rue_des_Rosiers%2C_Paris%2C_France_01.webp",
    "place-vosges.jpg": "https://segredosdeparis.com/wp-content/uploads/2021/03/Place_de_Vosges_em_Paris_de_Basile_Dell_et_Jeremie_Lippmann-1024x1024.jpg",
    "vintage-shop.jpg": "https://www.rucksack.se/wp-content/uploads/2023/02/Loppis-Paris-6.jpg",
    "milano-centrale.jpg": "https://primadituttomantova.it/media/2023/12/stazione-centrale-milano.jpg",
    "ostelzzz.jpg": "https://cdn.4travel.jp/img/thumbnails/imk/travelogue_pict/79/19/90/650x_79199053.jpg?updated_at=1697880754",
    "duomo-milano.jpg": "https://www.batiactu.com/images/auto/620-465-c/20120828_150937_duomo-milan1-jc-benoist.jpg",
    "galleria-milano.jpg": "https://sworld.it/img/img/70/photoAlbum/9383/originals/1.jpg",
    "scala-milano.jpg": "https://images.musement.com/cover/0165/39/thumb_16438887_cover_header.jpg",
    "brera.jpg": "https://staybook.in/_next/image?q=75&url=https%3A%2F%2Fcdn-imgix.headout.com%2Fmedia%2Fimages%2Fad45dbe7-4fd1-4827-9d2e-ec62568cc2e7-1756716623547-307352.jpg%3Fw%3D1120%26h%3D630%26crop%3Dfaces%26auto%3Dcompress%252Cformat%26fit%3Dmin&w=3840",
    "sforza.jpg": "https://amoitalia.com/wp2/wp-content/uploads/2020/05/milano_castello-sforzesco.jpg",
    "navigli.jpg": "https://cdn-imgix.headout.com/blog-content/image/80073a98fa31b8d080dfd51f624dd55c-Milan%20in%20September%20-%20Weather.jpg?ar=14%3A11&auto=compress%2Cformat&crop=faces&fit=crop&h=401.4&q=90&w=510.8727272727273",
    "malpensa-express.jpg": "https://www.cestee.es/images/93/02/189302-2560.jpeg",
    "azerbaijan-airlines.jpg": "https://images.cdn.centreforaviation.com/stories/new_image_database/airlines/azerbaijan_airlines/azal_azerbaijan_airlines_boeing_787_dreamliner-1024x.jpg",
    "nqz-airport.jpg": "https://rus.azattyq-ruhy.kz/cache/imagine/1200/uploads/news/2025/12/19/694589685f9d4065124657.jpg",
    "astana-mosque.jpg": "https://upload.wikimedia.org/wikipedia/en/0/00/Grand_Mosque_in_Astana%2C_Kazakhstan.jpg",
    "kazakhstan-museum.jpg": "https://commons.wikimedia.org/wiki/Special:FilePath/National%20Museum%20of%20Kazakhstan%2003.jpg",
    "baiterek.jpg": "https://images.unsplash.com/photo-1677842296338-eeb8c866d22c?auto=format&fit=crop&fm=jpg&q=80&w=1600",
    "khan-shatyr.jpg": "https://images.skyscrapercenter.com/building/khanshatyr_%28cc-by-nc-nd%29karim_yergaliyev.jpg",
    "flyarystan.webp": "https://ulysmedia.kz/cache/imagine/1200/uploads/news/2023/09/23/650eae60996c0971342025.webp",
    "urumqi-t4.jpg": "https://upload.wikimedia.org/wikipedia/commons/f/f3/%E4%B9%8C%E9%B2%81%E6%9C%A8%E9%BD%90%E5%A4%A9%E5%B1%B1%E5%9B%BD%E9%99%85%E6%9C%BA%E5%9C%BA%E8%88%AA%E7%AB%99%E6%A5%BC_Terminal_of_Urumqi_Tianshan_International_Airport.jpg",
}
headers = {"User-Agent": "Mozilla/5.0"}
for name, url in items.items():
    path = out / name
    try:
        r = requests.get(url, headers=headers, timeout=25, allow_redirects=True)
        r.raise_for_status()
        if len(r.content) < 10000:
            raise RuntimeError(f"too small: {len(r.content)} bytes")
        path.write_bytes(r.content)
        print("OK", name, len(r.content))
    except Exception as e:
        print("FAIL", name, repr(e))
