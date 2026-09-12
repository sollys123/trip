from pathlib import Path
import re

path = Path(r"E:\trip\france_trip_guide_2026.html")
text = path.read_text(encoding="utf-8")


def sub_once(pattern, repl, label):
    global text
    new, n = re.subn(pattern, lambda m: repl, text, count=1, flags=re.S)
    if n != 1:
        raise RuntimeError(f"{label}: expected 1 match, got {n}")
    text = new

# ---------- Global identity / hero ----------
text = text.replace('<title>法国旅行攻略 · 2026.09.29—10.10</title>', '<title>欧洲旅行攻略 · 2026.09.28—10.10</title>')
text = text.replace('content="杭州出发，经上海、德里前往巴黎和蔚蓝海岸的逐日旅行攻略，包含交通、住宿、餐饮、景点与出发前准备。"', 'content="杭州出发，经阿姆斯特丹、巴黎、蔚蓝海岸、米兰、阿斯塔纳前往乌鲁木齐的逐日旅行攻略，包含已出票交通、住宿、餐饮、景点与出发前准备。"')
text = text.replace('content:"PARIS  ·  NICE  ·  MENTON  ·  ÈZE"', 'content:"AMSTERDAM  ·  PARIS  ·  CÔTE D’AZUR  ·  MILAN  ·  ASTANA"')
text = text.replace('content:"PARIS"', 'content:"EUROPE"')
text = text.replace('content:"LA CÔTE D’AZUR\\A\\A carnet de voyage  ·  2026\\A 09.29 — 10.10"', 'content:"PARIS · CÔTE D’AZUR · MILAN\\A\\A carnet de voyage  ·  2026\\A 09.28 — 10.10"')
text = text.replace('France · 2026', 'Europe · 2026')
text = text.replace('PARIS × CÔTE D’AZUR · 2026.09.29—10.10', 'AMSTERDAM × PARIS × CÔTE D’AZUR × MILAN · 2026.09.28—10.10')
text = text.replace('巴黎 × 蔚蓝海岸<br>旅行攻略', '阿姆斯特丹 × 巴黎 × 南法 × 米兰<br>旅行攻略')
text = text.replace('杭州滨江出发 → 上海浦东 → 德里转机 → 巴黎 → 尼斯 / 芒通 / Villefranche / 摩纳哥 / Èze / 昂蒂布 → 巴黎 → 上海 → 杭州。', '杭州滨江出发 → 广州转机 → 阿姆斯特丹 → 巴黎 → 尼斯 / 芒通 / Villefranche / 摩纳哥 / Èze → 米兰 → 巴库 → 阿斯塔纳 → 乌鲁木齐。')
text = text.replace('<span>2026.09.29—10.10</span><span>Solo Voyage</span><span>巴黎与南法</span>', '<span>2026.09.28—10.10</span><span>Solo Voyage</span><span>荷兰 / 法国 / 意大利 / 哈萨克斯坦</span>')
text = text.replace('PARIS → NICE → PARIS', 'AMS → PARIS → NICE → MILAN → ASTANA')

# ---------- Overview ----------
overview = r'''<section><div class="container">
  <div class="section-head"><div><div class="eyebrow" style="color:var(--sea)">TRIP OVERVIEW</div><h2>行程概览</h2></div></div>
  <div class="grid-4">
    <div class="stat"><b>13天</b><span>9/28杭州出发 → 10/10乌鲁木齐抵达</span></div>
    <div class="stat"><b>5个主要停留地</b><span>阿姆斯特丹 / 巴黎 / 蔚蓝海岸 / 米兰 / 阿斯塔纳</span></div>
    <div class="stat"><b>4段已出票铁路</b><span>Eurostar / TGV / ZOU! / Intercity</span></div>
    <div class="stat"><b>5段已出票航班</b><span>南航2段 + 阿塞拜疆航空2段 + 飞狮1段</span></div>
  </div>
</div></section>'''
sub_once(r'<section><div class="container">\s*<div class="section-head"><div><div class="eyebrow" style="color:var\(--sea\)">TRIP OVERVIEW</div>.*?</section>', overview, 'overview')

# ---------- Budget ----------
budget = r'''<section id="budget"><div class="container">
  <div class="section-head"><div><div class="eyebrow" style="color:var(--sea)">BUDGET</div><h2>整体账单</h2></div><p>本版只把已经支付、已经出票或已经确认的固定成本写死；现场餐饮、市内交通和未预约景点继续保持动态，避免旧路线金额混进总账。</p></div>
  <div class="grid-4">
    <div class="stat"><b>≈¥12,146</b><span>当前已付 / 已锁定固定成本</span></div>
    <div class="stat"><b>¥3,811.86</b><span>巴黎 + 尼斯 + 米兰住宿预付</span></div>
    <div class="stat"><b>¥5,701</b><span>Air India 航变退款 · 已到账</span></div>
    <div class="stat"><b>€40.10</b><span>尼斯→巴黎夜火车 · 已退款</span></div>
  </div>

  <h3 style="margin-top:30px">已付 / 已确定固定支出</h3>
  <div class="tablewrap"><table><thead><tr><th>类别</th><th>项目</th><th>金额</th><th>状态 / 备注</th></tr></thead><tbody>
    <tr><td>国际机票</td><td>杭州 → 广州 → 阿姆斯特丹 · CZ3802 + CZ307</td><td><b>¥2,668</b></td><td><span class="badge locked">已出票</span> 8kg手提 + 23kg托运；广州联程不取行李</td></tr>
    <tr><td>国际机票</td><td>米兰 → 巴库 → 阿斯塔纳 → 乌鲁木齐</td><td><b>¥2,338</b></td><td><span class="badge locked">已出票</span> J2036 + J28049 + FS7961</td></tr>
    <tr><td>取消损失</td><td>原 Air India 订单未退部分</td><td><b>¥432</b></td><td>原订单¥6,133；航变退款¥5,701已到账</td></tr>
    <tr><td>住宿</td><td>The People – Paris Bercy · 9/29→9/30</td><td><b>¥496.05</b></td><td>6人女生宿舍；城市税另付约¥20.28</td></tr>
    <tr><td>住宿</td><td>The People – Paris Bercy · 9/30→10/3</td><td><b>¥1,559.34</b></td><td>原6人女生宿舍订单保留；城市税另付约¥60.60</td></tr>
    <tr><td>住宿</td><td>SLO Nice · 10/3→10/4</td><td><b>¥356.23</b></td><td>8人混住宿舍</td></tr>
    <tr><td>住宿</td><td>SLO Nice · 10/4→10/7</td><td><b>¥1,071.28</b></td><td>4人女生宿舍</td></tr>
    <tr><td>住宿</td><td>Ostelzzz Milano · 10/7→10/8</td><td><b>¥328.96</b></td><td>女生宿舍床位；城市税另付约¥23.37</td></tr>
    <tr><td>铁路</td><td>Eurostar 9476 · Amsterdam → Paris</td><td><b>约¥259</b></td><td>购票时展示HK$302.84；6车64座</td></tr>
    <tr><td>铁路</td><td>TGV INOUI 6177 · Paris → Nice</td><td><b>€47</b></td><td><span class="badge locked">已出票</span></td></tr>
    <tr><td>铁路</td><td>ZOU! 86007 · Nice → Ventimiglia</td><td><b>€10.60</b></td><td><span class="badge locked">已出票</span></td></tr>
    <tr><td>铁路</td><td>Intercity 631 · Ventimiglia → Milano</td><td><b>€27.90 + €1</b></td><td>Economy 2等座 + tiRimborso退款选项</td></tr>
    <tr><td>景点</td><td>Louvre + Musée d’Orsay 夜场</td><td><b>€32 + €12</b></td><td><span class="badge locked">已购票</span></td></tr>
    <tr><td>签证/保险</td><td>法国签证费 + TLS服务/Prime Time/快递 + 申根保险</td><td><b>¥1,618</b></td><td>签证相关¥1,348 + 保险¥270</td></tr>
  </tbody></table></div>

  <h3 style="margin-top:30px">仍需现场支付 / 尚未购买</h3>
  <div class="tablewrap"><table><thead><tr><th>类别</th><th>项目</th><th>当前状态</th></tr></thead><tbody>
    <tr><td>城市税</td><td>巴黎新增一晚约¥20.28 + 原巴黎约¥60.60 + 米兰约¥23.37 + 尼斯当地税</td><td>到店支付</td></tr>
    <tr><td>阿姆斯特丹</td><td>Schiphol→Centraal 火车、行李寄存、Rijksmuseum、运河游船</td><td><span class="badge check">博物馆待预约</span> 游船可晚些买</td></tr>
    <tr><td>市内/区域交通</td><td>巴黎、南法、米兰、阿斯塔纳当地交通</td><td>按当天实际购买</td></tr>
    <tr><td>景点</td><td>Jardin Exotique d’Èze、米兰 Duomo（屋顶仅按兴趣选）</td><td>未购买</td></tr>
    <tr><td>餐饮</td><td>巴黎、尼斯、米兰、阿斯塔纳餐饮与超市</td><td>现场支出</td></tr>
  </tbody></table></div>
  <div class="notice sea"><strong>退款已收口：</strong>Air India 已到账 ¥5,701；Nice→Paris 夜火车 €40.10 已取消退款。两项均不再属于当前有效行程。</div>
</div></section>'''
sub_once(r'<section id="budget">.*?</section>', budget, 'budget')

# ---------- Bookings ----------
bookings = r'''<section id="bookings"><div class="container">
  <div class="section-head"><div><div class="eyebrow" style="color:var(--sea)">BOOKINGS</div><h2>已预订的交通与住宿</h2></div><p>这里以实际出票/确认单为准，旧 Air India 与 Nice→Paris 夜车已经退款，不再作为有效订单展示。</p></div>

  <h3>航班 · Flights</h3>
  <div class="tablewrap"><table><thead><tr><th>日期</th><th>航班</th><th>航段</th><th>当地时间</th><th>航站楼</th><th>状态</th></tr></thead><tbody>
    <tr><td>9/28</td><td><b>CZ3802</b></td><td>杭州 HGH → 广州 CAN</td><td>21:35 → 23:50</td><td>HGH T4 → CAN T2</td><td><span class="badge locked">已出票</span></td></tr>
    <tr><td>9/29</td><td><b>CZ307</b></td><td>广州 CAN → 阿姆斯特丹 AMS</td><td>01:55 → 08:00</td><td>CAN T2 → AMS</td><td><span class="badge locked">已出票</span></td></tr>
    <tr><td>10/8</td><td><b>J2036</b></td><td>米兰 MXP → 巴库 GYD</td><td>11:25 → 18:05</td><td>MXP T1 → GYD T1</td><td><span class="badge locked">已出票</span></td></tr>
    <tr><td>10/8 → 10/9</td><td><b>J28049</b></td><td>巴库 GYD → 阿斯塔纳 NQZ</td><td>22:00 → 02:00 +1</td><td>GYD T1 → NQZ T1</td><td><span class="badge locked">已出票</span></td></tr>
    <tr><td>10/9 → 10/10</td><td><b>FS7961</b></td><td>阿斯塔纳 NQZ → 乌鲁木齐 URC</td><td>22:30 → 03:55 +1</td><td>NQZ T1 → URC</td><td><span class="badge locked">已出票</span></td></tr>
  </tbody></table></div>
  <div class="notice"><strong>去程：</strong>CZ3802 + CZ307 为联程，广州转机2小时05分，确认单写明无需领取并重新托运行李；免费行李为1件8kg手提 + 1件23kg托运。携程订单总金额 ¥2,668，航司预订号 PF6EJR。</div>
  <div class="notice"><strong>返程：</strong>MXP→GYD→NQZ 前两段阿塞拜疆航空免费1件10kg手提 + 1件23kg托运；NQZ→URC 为飞狮航空，确认单显示1件20kg托运。阿斯塔纳停留20小时30分，订单提示该处<strong>可能需要领取并重新托运行李</strong>，到米兰值机时必须确认行李标签最终目的地。</div>

  <h3 style="margin-top:30px">长途铁路 · Trains</h3>
  <div class="tablewrap"><table><thead><tr><th>日期</th><th>列车</th><th>路线</th><th>时间</th><th>座位 / 票务</th><th>备注</th></tr></thead><tbody>
    <tr><td>9/29 周二</td><td><b>Eurostar 9476</b></td><td>Amsterdam Centraal → Paris Gare du Nord</td><td><b>17:10 → 20:40</b></td><td>Standard · 6车64座<br>PNR MCMMDY</td><td><span class="badge locked">已出票</span> 官方票面要求16:50前到站；2件≤75cm行李 + 1件小随身包</td></tr>
    <tr><td>10/3 周六</td><td><b>TGV INOUI 6177</b></td><td>Paris Gare de Lyon → Nice Ville</td><td><b>14:10 → 约20:04</b></td><td>€47</td><td><span class="badge locked">已出票</span></td></tr>
    <tr><td>10/7 周三</td><td><b>ZOU! 86007</b></td><td>Nice Ville → Ventimiglia</td><td><b>07:23 → 08:21</b></td><td>2等座 · €10.60<br>Ref U21WR7</td><td><span class="badge locked">已出票</span> 49分钟换乘余量</td></tr>
    <tr><td>10/7 周三</td><td><b>Intercity 631</b></td><td>Ventimiglia → Milano Centrale</td><td><b>09:10 → 13:00</b></td><td>2等 Classe Easy · 6车16A<br>PNR XE6CV5</td><td><span class="badge locked">已出票</span> Economy票出发前可改；本票另购€1 tiRimborso</td></tr>
  </tbody></table></div>
  <div class="notice sea"><strong>Eurostar退改：</strong>票面写明出发前1小时可免改签手续费（补票差）；出发日前7天以前退票收€25/£25/$40每人每程。尼斯→文蒂米利亚票面为不可改、最晚出发前一天通过原渠道办理退款；IC631 Economy常规不可退，本票已附€1 tiRimborso选项。</div>

  <h3 style="margin-top:30px">住宿 · Stays</h3>
  <div class="grid-3">
    <div class="card"><span class="badge locked">巴黎 · 两笔订单</span><h3>The People – Paris Bercy</h3><p><b>9/29→9/30：</b>6人女生宿舍，已付 <b>¥496.05</b>，城市税约¥20.28。<br><b>9/30→10/3：</b>原6人女生宿舍订单保留，已付 <b>¥1,559.34</b>，城市税约¥60.60。</p><p>地址：28 Boulevard de Reuilly。新增单入住窗口15:00–次日00:30，退房最晚10:30。到店时把两笔订单一起给前台看，争取连续留在同一床位；不能保证时，9/30白天寄存行李再换床。</p><div class="btnrow"><a class="btn" href="https://www.thepeoplehostel.com/en/destinations/paris-bercy/" target="_blank">官方住宿页</a><a class="btn light" href="https://www.google.com/maps/search/?api=1&query=The%20People%20Paris%20Bercy%2028%20Boulevard%20de%20Reuilly%20Paris" target="_blank">地图</a></div></div>
    <div class="card"><span class="badge locked">尼斯 · 两笔订单</span><h3>SLO Nice</h3><p><b>10/3→10/4：</b>8人混住宿舍，¥356.23；<br><b>10/4→10/7：</b>4人女生宿舍，¥1,071.28。</p><p>地址：20 Rue de Paris。10/4先退旧床、寄存行李，晚上入住女生房。客用冰箱、微波炉和餐具已确认。</p><div class="btnrow"><a class="btn" href="https://slohostels.com/en/nice/" target="_blank">SLO Nice 官方</a><a class="btn light" href="https://www.google.com/maps/search/?api=1&query=SLO%20Nice%2020%20Rue%20de%20Paris%20Nice" target="_blank">地图</a></div></div>
    <div class="card"><span class="badge locked">米兰 · 已订</span><h3>Ostelzzz Milano</h3><p><b>10/7→10/8：</b>女生上下铺宿舍单床位，已付 <b>¥328.96</b>；到店城市税 USD3.48，约¥23.37。地址：Via Giorgio Jan 5A。</p><p>入住15:00以后，退房11:00以前；订单为预付且自行取消会扣全额预付款。确认单无餐食。</p><div class="btnrow"><a class="btn" href="https://www.ostelzzz.com/" target="_blank">Ostelzzz 官方</a><a class="btn light" href="https://www.google.com/maps/search/?api=1&query=Ostelzzz%20Milano%20Via%20Giorgio%20Jan%205A" target="_blank">地图</a></div></div>
  </div>
  <div class="notice sea"><strong>阿姆斯特丹不住宿：</strong>9/29早上落地后白天游览，下午直接从 Amsterdam Centraal 搭 Eurostar 去巴黎。原“阿姆斯特丹住一晚”的方案已取消。</div>
</div></section>'''
sub_once(r'<section id="bookings">.*?</section>', bookings, 'bookings')

# ---------- Local transport ----------
transport = r'''<section id="transport"><div class="container">
  <div class="section-head"><div><div class="eyebrow" style="color:var(--sea)">PASSES & TRANSIT</div><h2>市内交通与通票</h2></div><p>长途票已经锁定；这里仅保留到当地再处理的小交通。</p></div>
  <div class="grid-3">
    <div class="card"><h3>阿姆斯特丹 · 9/29</h3><p><b>Schiphol → Amsterdam Centraal</b> 机场火车约15–20分钟。无需提前买票，可直接用支持非接触支付的银行卡/手机进出站；进出站必须使用同一张卡/同一设备。</p><p>到中央站先寄存行李，再去国立博物馆和运河区域；16:20左右回站取行李。</p></div>
    <div class="card"><h3>巴黎 · 9/29–10/3</h3><p>当前整段都落在同一个周一至周日周期，<b>Navigo Semaine</b> 仍可作为候选；是否购买按实际乘车次数决定。现在不再包含CDG机场往返。</p><a href="https://www.iledefrance-mobilites.fr/en/titres-et-tarifs/detail/forfait-navigo-semaine" target="_blank">Île-de-France Mobilités →</a></div>
    <div class="card"><h3>南法 · 10/4–10/6</h3><p><b>Pass SudAzur Explore 3日</b> 继续覆盖尼斯、芒通、Villefranche、摩纳哥、Èze 的主要 TER / 公交 / 电车。10/7已改为单独出票前往意大利，不再去Antibes。</p><a href="https://www.ter.sncf.com/sud-provence-alpes-cote-d-azur/tarifs-cartes/bons-plans/pass-sudazur-explore-en" target="_blank">SNCF 官方介绍 →</a></div>
    <div class="card"><h3>米兰 · 10/7–10/8</h3><p>Ostelzzz位于Lima / Porta Venezia一带。市区优先地铁；10/8早上回 Milano Centrale 后乘 <b>Malpensa Express</b> 前往 MXP T1，目标08:45–09:00前抵达机场。</p><a href="https://www.malpensaexpress.it/en/" target="_blank">Malpensa Express →</a></div>
    <div class="card"><h3>阿斯塔纳 · 10/9</h3><p>凌晨02:00落地后先在机场安全区域休息，天亮后再进城。当天跨点较分散，优先打车/网约车，晚上18:30–19:00左右回机场准备22:30航班。</p></div>
  </div>
</div></section>'''
sub_once(r'<section id="transport">.*?</section>', transport, 'transport')

# ---------- Daily itinerary: 9/28 + 9/29 ----------
d0928_0929 = r'''<article class="day" id="d0928"><div class="dayhead"><div><h3>9/28 周一 · 杭州 → 广州 → 阿姆斯特丹</h3><div class="sub">新去程从杭州直接出发，经广州联程前往阿姆斯特丹，不再去上海浦东。</div></div><div class="walk"><b>转场日</b>步行强度 ★☆☆☆☆</div></div>
  <div class="route-ribbon"><span>滨江</span><i class="arrow">→</i><span>HGH T4</span><i class="arrow">→</i><span>CZ3802</span><i class="arrow">→</i><span>CAN T2</span><i class="arrow">→</i><span>CZ307</span></div>
  <div class="timeline">
    <div class="step"><div class="time">17:30–18:20</div><h4>滨江 → 杭州萧山机场 T4</h4><p>直接网约车前往HGH T4。国际联程建议至少提前约3小时到机场，护照、签证、返程机票和住宿确认单放在随身小包。</p></div>
    <div class="step"><div class="time">18:20–20:45</div><h4>值机、托运行李、安检</h4><p>确认行李牌是否直接挂到 AMS。确认单写明广州联程无需领取并重新托运行李。</p></div>
    <div class="step"><div class="time">21:35–23:50</div><h4>CZ3802 · HGH T4 → CAN T2</h4><p>经济舱。免费行李：1件8kg手提 + 1件23kg托运。</p></div>
    <div class="step"><div class="time">23:50–01:55</div><h4>广州白云 T2 · 联程转机 2小时05分</h4><p>不取托运行李，按国际转机指引前往下一程登机口。</p></div>
  </div></article>

  <article class="day" id="d0929"><div class="dayhead"><div><h3>9/29 周二 · 阿姆斯特丹一日 → Eurostar → 巴黎</h3><div class="sub">不在阿姆斯特丹住宿：保留国立博物馆 + 运河体验，下午直接进巴黎。</div></div><div class="walk"><b>约 6–8 km</b>长途飞行后控制强度 · ★★★☆☆</div></div>
  <div class="route-ribbon"><span>AMS</span><i class="arrow">→</i><span>Centraal寄存</span><i class="arrow">→</i><span>Rijksmuseum</span><i class="arrow">→</i><span>Canal</span><i class="arrow">→</i><span>Eurostar 9476</span><i class="arrow">→</i><span>Paris Nord</span><i class="arrow">→</i><span>Bercy</span></div>
  <div class="timeline">
    <div class="step"><div class="time">01:55–08:00</div><h4>CZ307 · CAN T2 → AMS</h4><p>尽量在航班后半段休息，08:00当地时间抵达史基浦机场。</p></div>
    <div class="step"><div class="time">08:00–10:00</div><h4>入境、取行李 → Amsterdam Centraal</h4><p>按正常速度预留边检和取行李时间；随后乘机场火车进中央站。到站先寄存大件行李，再开始市区游览。</p></div>
    <div class="step"><div class="time">10:30–12:45</div><h4>Rijksmuseum · 国立博物馆</h4><p><span class="badge check">待预约</span> 目标预约10:30左右入场。控制在2–2.5小时，优先 Gallery of Honour、Rembrandt、Vermeer 等核心馆藏。</p><div class="btnrow"><a class="btn" href="https://www.rijksmuseum.nl/en/tickets" target="_blank">官方订票</a></div></div>
    <div class="step"><div class="time">13:00–13:45</div><h4>午餐 + 运河区步行</h4><p>不专门绕路找餐厅，在博物馆区到运河登船点之间解决午餐。</p></div>
    <div class="step"><div class="time">14:00–15:10</div><h4>Amsterdam Canal Cruise</h4><p>游船保留弹性，不要买无法改的过早班次；如果CZ307明显晚点，优先保国立博物馆，游船可直接删除。</p></div>
    <div class="step"><div class="time">15:10–16:20</div><h4>回 Amsterdam Centraal · 取行李</h4><p>16:20左右进入车站流程，避免把下午最后一段压得太紧。</p></div>
    <div class="step"><div class="time">16:50–17:10</div><h4>Eurostar 9476 · 候车 / 登车</h4><p>票面要求16:50前到站；Standard，6车64座，PNR MCMMDY。</p></div>
    <div class="step"><div class="time">17:10–20:40</div><h4>Eurostar 9476 · Amsterdam → Paris Nord</h4><p>直达 Paris Gare du Nord。行李限额：2件不超过75cm的行李 + 1件小随身包，需自行搬运。</p></div>
    <div class="step"><div class="time">20:40–21:45</div><h4>Paris Nord → The People Bercy</h4><p>按实时导航乘地铁前往 Daumesnil / Reuilly 一带。这个到达时间比原22:43方案宽松很多。</p></div>
    <div class="step"><div class="time">21:45–22:30</div><h4>入住 The People – Paris Bercy</h4><p>9/29单晚为单独订单，但同样是6人女生宿舍。把9/29与9/30起的两笔确认号一起给前台，询问能否连续使用同一床位。</p></div>
  </div></article>'''
sub_once(r'<article class="day" id="d0929">.*?</article>', d0928_0929, 'd0928_d0929')

# ---------- Daily itinerary: 9/30 ----------
d0930 = r'''<article class="day" id="d0930"><div class="dayhead"><div><h3>9/30 周三 · 蒙马特 → 圣心堂 → Opéra / Haussmann</h3><div class="sub">提前一天进巴黎以后，9/30变成完整巴黎日；今天只做北巴黎 + 歌剧院商圈，不和后面左岸、卢浮宫重复。</div></div><div class="walk"><b>约 7–9 km</b>可随时缩短 · ★★★☆☆</div></div>
  <div class="route-ribbon"><span>Bercy</span><i class="arrow">→</i><span>Montmartre</span><i class="arrow">→</i><span>Sacré-Cœur</span><i class="arrow">→</i><span>Opéra</span><i class="arrow">→</i><span>Galeries Lafayette</span><i class="arrow">→</i><span>Bercy</span></div>
  <div class="timeline">
    <div class="step"><div class="time">08:30–09:15</div><h4>早餐 + 处理两笔住宿订单衔接</h4><p>先问前台能否直接保留原床位。如果必须换床，10:30前退掉9/29这一单，把行李寄存在前台，晚上再办理原9/30–10/3订单。</p></div>
    <div class="step"><div class="time">09:30–11:45</div><h4>Montmartre + Sacré-Cœur</h4><p>从山下慢慢走上去，游览圣心堂与蒙马特街区；今天没有后续硬预约，不需要赶。</p></div>
    <div class="step"><div class="time">12:00–13:00</div><h4>蒙马特 / 南下途中午餐</h4><p>就近解决，优先热食或面包店，不为了某一家餐厅绕路。</p></div>
    <div class="step"><div class="time">13:15–16:30</div><h4>Palais Garnier 外观 → Galeries Lafayette</h4><p>看巴黎歌剧院外观，再逛 Haussmann 商圈和老佛爷。屋顶免费时可顺路上去，不单独为屋顶改动整天路线。</p></div>
    <div class="step"><div class="time">16:30–18:30</div><h4>自由时间 / 咖啡 / 提前回青旅</h4><p>第一天跨洲飞行后可能仍然疲劳，下午不再硬塞博物馆；按体力决定继续逛或直接回Bercy休息。</p></div>
    <div class="step"><div class="time">18:30–20:00</div><h4>超市补给 + 晚餐</h4><p>为10/1–10/3补充早餐、酸奶、微波餐和火车零食。之后早点休息。</p></div>
  </div></article>'''
sub_once(r'<article class="day" id="d0930">.*?</article>', d0930, 'd0930')

# ---------- Daily itinerary: 10/7 ----------
d1007 = r'''<article class="day" id="d1007"><div class="dayhead"><div><h3>10/7 周三 · 尼斯 → 文蒂米利亚 → 米兰</h3><div class="sub">Antibes 与巴黎夜车方案取消。今天用早班铁路直达米兰，下午一次性按地理顺序游览市中心。</div></div><div class="walk"><b>约 7–9 km</b>早起 + 半日米兰 · ★★★★☆</div></div>
  <div class="route-ribbon"><span>SLO Nice</span><i class="arrow">→</i><span>Nice Ville</span><i class="arrow">→</i><span>Ventimiglia</span><i class="arrow">→</i><span>Milano Centrale</span><i class="arrow">→</i><span>Ostelzzz</span><i class="arrow">→</i><span>Duomo</span><i class="arrow">→</i><span>Brera</span><i class="arrow">→</i><span>Sforza</span><i class="arrow">→</i><span>Navigli</span></div>
  <div class="timeline">
    <div class="step"><div class="time">06:10–06:50</div><h4>退房 + 步行去 Nice Ville</h4><p>前一晚把早餐和水准备好。SLO离车站很近，06:50左右进入车站即可。</p></div>
    <div class="step"><div class="time">07:23–08:21</div><h4>ZOU! 86007 · Nice Ville → Ventimiglia</h4><p>已出票，2等座，€10.60，Ref U21WR7。</p></div>
    <div class="step"><div class="time">08:21–09:10</div><h4>Ventimiglia · 49分钟换乘</h4><p>两段为分开出票，抵达后先确认IC631站台；不要离站吃正式早餐，只做厕所、补水和简单食物。</p></div>
    <div class="step"><div class="time">09:10–13:00</div><h4>Intercity 631 · Ventimiglia → Milano Centrale</h4><p>2等 Classe Easy，6车16A，PNR XE6CV5。Economy常规不可退，本票另有€1 tiRimborso服务。</p></div>
    <div class="step"><div class="time">13:00–13:50</div><h4>Milano Centrale → Ostelzzz · 寄存行李</h4><p>酒店15:00后入住；先寄存行李，不等房间。地址 Via Giorgio Jan 5A。</p></div>
    <div class="step"><div class="time">14:10–15:40</div><h4>Duomo di Milano · 外观 + 内部</h4><p>先在广场看完整哥特立面与尖塔群，再进入教堂。<b>屋顶只是可选项：</b>如果想近距离走进飞扶壁和石雕之间，就在这一次参观里一起上；不为了屋顶二次折返。</p><div class="btnrow"><a class="btn" href="https://www.duomomilano.it/en/" target="_blank">Duomo 官方</a></div></div>
    <div class="step"><div class="time">15:40–16:10</div><h4>Galleria Vittorio Emanuele II</h4><p>从Duomo广场直接进入拱廊，顺路穿过去。</p></div>
    <div class="step"><div class="time">16:10–16:30</div><h4>Teatro alla Scala · 外观 / 广场</h4><p>不专门进馆，作为从Galleria前往Brera的顺路线节点。</p></div>
    <div class="step"><div class="time">16:30–17:30</div><h4>Brera 街区</h4><p>以街区、小店、咖啡馆和城市氛围为主；前面已有Rijksmuseum、奥赛和卢浮宫，因此默认不再硬塞Brera美术馆。</p></div>
    <div class="step"><div class="time">17:35–18:25</div><h4>Castello Sforzesco · 城堡庭院 / 外部</h4><p>从Brera继续往西走，不折返Duomo。重点看城堡建筑与庭院。</p></div>
    <div class="step"><div class="time">18:40以后</div><h4>Navigli / Darsena · 晚饭 + 夜景</h4><p>晚上到运河区吃饭和散步，再回 Ostelzzz。今天不安排《最后的晚餐》：官方常规票已满，也不把行程绑定在临时放票上。</p></div>
  </div></article>'''
sub_once(r'<article class="day" id="d1007">.*?</article>', d1007, 'd1007')

# ---------- Daily itinerary: 10/8 ----------
d1008 = r'''<article class="day" id="d1008"><div class="dayhead"><div><h3>10/8 周四 · 米兰 → 巴库 → 阿斯塔纳</h3><div class="sub">早上直接去马尔彭萨机场，开始返程；不再返回巴黎。</div></div><div class="walk"><b>机场转场日</b>步行强度 ★☆☆☆☆</div></div>
  <div class="timeline">
    <div class="step"><div class="time">06:45–07:20</div><h4>起床、早餐、退房</h4><p>Ostelzzz订单无餐食，不依赖青旅早餐；提前准备面包/酸奶或途中购买。</p></div>
    <div class="step"><div class="time">07:20–08:50</div><h4>Ostelzzz → Milano Centrale → MXP T1</h4><p>先回 Milano Centrale，再乘 Malpensa Express。具体班次出发前确认，目标<b>08:45–09:00前抵达 T1</b>，给11:25国际航班留足值机、退税和安检时间。</p><div class="btnrow"><a class="btn" href="https://www.malpensaexpress.it/en/" target="_blank">Malpensa Express</a></div></div>
    <div class="step"><div class="time">11:25–18:05</div><h4>J2036 · MXP T1 → GYD T1</h4><p>阿塞拜疆航空。免费1件10kg手提 + 1件23kg托运。</p></div>
    <div class="step"><div class="time">18:05–22:00</div><h4>巴库转机 · 3小时55分</h4><p>前两段订单显示无需领取并重新托运行李；仍在米兰值机时再次确认行李牌是否挂到NQZ。</p></div>
    <div class="step"><div class="time">22:00–02:00</div><h4>J28049 · GYD T1 → NQZ T1</h4><p>10/9凌晨02:00抵达阿斯塔纳。</p></div>
  </div></article>'''
sub_once(r'<article class="day" id="d1008">.*?</article>', d1008, 'd1008')

# ---------- Daily itinerary: 10/9 + 10/10 ----------
d1009_1010 = r'''<article class="day" id="d1009"><div class="dayhead"><div><h3>10/9 周五 · 阿斯塔纳停留约20小时 → 乌鲁木齐</h3><div class="sub">凌晨落地不进城乱走；先在机场休息，天亮后再用一整天看阿斯塔纳核心地标。</div></div><div class="walk"><b>约 5–7 km</b>分散景点以打车为主 · ★★★☆☆</div></div>
  <div class="route-ribbon"><span>NQZ</span><i class="arrow">→</i><span>Grand Mosque</span><i class="arrow">→</i><span>National Museum</span><i class="arrow">→</i><span>Bayterek / Nurzhol</span><i class="arrow">→</i><span>Khan Shatyr</span><i class="arrow">→</i><span>NQZ</span></div>
  <div class="timeline">
    <div class="step"><div class="time">02:00–06:30</div><h4>NQZ T1 · 入境 / 行李 / 机场休息</h4><p>订单提示阿斯塔纳段<strong>可能需要领取并重新托运行李</strong>。先确认行李状态；凌晨不安排市区活动，在有工作人员和其他旅客的区域休息到天亮。</p></div>
    <div class="step"><div class="time">07:00–08:30</div><h4>进城 + 早餐</h4><p>优先网约车/出租车，避免带着行李反复研究公交。大件行李若需随身，先确认机场寄存或航空公司可提前托运时间。</p></div>
    <div class="step"><div class="time">09:00–10:30</div><h4>Astana Grand Mosque</h4><p>重点看巨大的蓝色穹顶和内部空间。女性准备能覆盖头发的围巾，衣着遮肩遮膝，入内脱鞋。</p></div>
    <div class="step"><div class="time">10:45–12:15</div><h4>National Museum / 周边</h4><p>按当天开放情况决定是否进馆；如果疲劳，就只看外部与附近城市轴线。</p></div>
    <div class="step"><div class="time">12:30–15:30</div><h4>Bayterek → Nurzhol Boulevard · 午餐</h4><p>看阿斯塔纳新城核心轴线，午餐放在这一片解决。</p></div>
    <div class="step"><div class="time">15:45–17:30</div><h4>Khan Shatyr</h4><p>作为下午最后一站，天气不好时也可以在室内休息。</p></div>
    <div class="step"><div class="time">18:00–19:00</div><h4>返回 NQZ</h4><p>给晚间国际航班留足值机、重新托运行李和边检时间。</p></div>
    <div class="step"><div class="time">22:30–03:55</div><h4>FS7961 · NQZ T1 → URC</h4><p>飞狮航空，订单显示1件20kg托运行李。10/10凌晨03:55抵达乌鲁木齐。</p></div>
  </div></article>

  <article class="day" id="d1010"><div class="dayhead"><div><h3>10/10 周六 · 乌鲁木齐抵达</h3><div class="sub">本次欧洲 / 中亚行程正式结束。</div></div><div class="walk"><b>抵达日</b>步行强度 ★☆☆☆☆</div></div>
  <div class="timeline">
    <div class="step"><div class="time">03:55–05:30</div><h4>URC · 入境 / 取行李</h4><p>完成中国入境、海关和取行李后离开机场。后续乌鲁木齐市内交通按实际住宿/接人安排处理。</p></div>
  </div></article>'''
sub_once(r'<article class="day" id="d1009">.*?</article>', d1009_1010, 'd1009_d1010')

# ---------- Food section ----------
food = r'''<section id="food"><div class="container">
  <div class="section-head"><div><div class="eyebrow" style="color:var(--sea)">FOOD DATABASE</div><h2>餐饮清单</h2></div><p>只保留当前路线仍会经过的餐饮点；米兰10/7晚餐不锁死餐厅，直接放在Navigli / Darsena现场选择。</p></div>
  <div class="grid-3">
    <div class="card food"><h3>Truffes Folies Paris 7</h3><div class="rating">TheFork 9.5/10 · 7,326评</div><p>10/2 午餐 · 37 Rue Malar</p><div class="order"><b>推荐：</b>truffle pasta / risotto / ravioli。</div><div class="btnrow"><a class="btn light" href="https://www.thefork.com/restaurant/truffes-folies-7eme-r3597" target="_blank">菜单/预订</a></div></div>
    <div class="card food"><h3>Le Bistro Dalpozzo</h3><div class="rating">TheFork 9.1/10 · 1,139评</div><p>10/4 晚餐 · Nice</p><div class="order"><b>推荐：</b>Boeuf braisé au Chianti / 牛脸颊等浓汁肉；备选 gnocchi à la daube。</div></div>
    <div class="card food"><h3>Chez Thérésa</h3><div class="rating">尼斯传统 socca · 适合外带</div><p>10/4 中午 · Cours Saleya / rue Droite</p><div class="order"><b>推荐：</b>socca，可加 pissaladière。</div></div>
    <div class="card food"><h3>BO&MIE Saint-Michel</h3><div class="rating">左岸 · 拉丁区 / 圣母院顺路</div><p>10/1 午餐 · 5–7 boulevard Saint-Michel</p><div class="order"><b>推荐：</b>quiche、三明治或当日烘焙。</div></div>
    <div class="card food"><h3>Tutti Frutti</h3><div class="rating">Menton · Rue Saint-Michel</div><p>10/5 芒通老城</p><div class="order">想吃当地柠檬口味时顺路买 lemon sorbet。</div></div>
    <div class="card food"><h3>Navigli / Darsena 晚餐</h3><div class="rating">10/7 · Milan</div><p>Duomo → Brera → Sforza 之后继续往南到运河区。</p><div class="order">不提前锁一家餐厅；按当天体力和排队情况，在Navigli附近选择意面、risotto、cotoletta或aperitivo正餐。</div></div>
  </div>
</div></section>'''
sub_once(r'<section id="food">.*?</section>', food, 'food')

# ---------- Grocery stale references ----------
text = text.replace('长途火车、摩纳哥/Èze 和夜车前优先买不容易漏汁的款。', '长途火车、摩纳哥/Èze 和10/7尼斯→米兰早班车前优先买不容易漏汁的款。')
text = text.replace('9/30晚、10/3早午餐、尼斯晚间备用', '巴黎晚间、10/3早午餐、尼斯晚间备用')
text = text.replace('转场、10/6午餐、10/7夜车', '转场、10/6午餐、10/7尼斯→米兰早班火车')

# ---------- Safety ----------
safety = r'''<section id="safety"><div class="container">
  <div class="section-head"><div><div class="eyebrow" style="color:var(--sea)">SAFETY & LANGUAGE</div><h2>安全与语言</h2></div><p>这版重点放在独自旅行、行李转场和阿斯塔纳凌晨抵达。</p></div>
  <div class="grid-2">
    <div class="card"><h3>巴黎 / 米兰防盗</h3><ul class="checklist"><li>地铁、火车站和热门景点人多时把包放在身体前侧</li><li>手机不放后裤袋或外套外袋，车门附近尽量少低头刷手机</li><li>咖啡馆内不要把手机放桌边</li><li>护照、主银行卡和备用卡分开放置</li><li>青旅储物柜上锁，自带可靠小锁</li><li>Milano Centrale、Paris Nord 只做正常换乘，不在陌生人主动搭话时展示票据或钱包</li></ul></div>
    <div class="card"><h3>阿斯塔纳凌晨抵达</h3><ul class="checklist"><li>02:00落地后先完成入境与行李确认，不凌晨独自在市区游荡</li><li>在灯光充足、有工作人员或其他旅客的机场区域休息到天亮</li><li>如需重新托运行李，先问清最早可办理时间</li><li>进城优先正规出租车 / 网约车</li><li>大清真寺准备围巾，衣着遮肩遮膝</li><li>18:00左右开始回机场，给22:30航班留足余量</li></ul></div>
  </div>
  <div class="notice sea"><strong>保险提醒：</strong>旧方案保险日期是9/29–10/8；新行程已变成9/28出发、10/10抵达，并增加哈萨克斯坦停留。若希望获得全程旅行保障，出发前确认保单能否延长到9/28–10/10并覆盖哈萨克斯坦。</div>
  <h3 style="margin-top:30px">常用法语表达</h3>
  <div class="card flat"><div class="phrase"><b>Bonjour !</b><span>你好（进店/问人前先说）</span></div><div class="phrase"><b>Bonsoir !</b><span>晚上好</span></div><div class="phrase"><b>Excusez-moi.</b><span>不好意思 / 打扰一下</span></div><div class="phrase"><b>Vous parlez anglais ?</b><span>你说英语吗？</span></div><div class="phrase"><b>S'il vous plaît.</b><span>请</span></div><div class="phrase"><b>Merci beaucoup.</b><span>非常感谢</span></div><div class="phrase"><b>Au revoir.</b><span>再见</span></div><div class="phrase"><b>L'addition, s'il vous plaît.</b><span>请结账</span></div></div>
</div></section>'''
sub_once(r'<section id="safety">.*?</section>', safety, 'safety')

# ---------- Jet lag ----------
jetlag = r'''<section id="jetlag"><div class="container">
  <div class="section-head"><div><div class="eyebrow" style="color:var(--sea)">SLEEP & JET LAG</div><h2>长途交通期间的睡眠安排</h2></div></div>
  <div class="grid-2">
    <div class="card"><h3>去程 · 杭州 → 广州 → 阿姆斯特丹</h3><ol><li>9/28晚杭州起飞后不必强行熬夜，广州转机保持清醒。</li><li>CZ307起飞后吃完第一轮餐，尽量连续睡一段。</li><li>靠近阿姆斯特丹当地清晨时逐步醒来，落地后接触自然光。</li><li>9/29阿姆斯特丹只安排Rijksmuseum + 游船，不再塞第二个大馆。</li><li>20:40到巴黎后直接入住，尽量23:00前后睡。</li></ol></div>
    <div class="card"><h3>返程 · 米兰 → 巴库 → 阿斯塔纳 → 乌鲁木齐</h3><ol><li>10/8从米兰出发后按机上时间休息，不追求一次睡够。</li><li>10/9凌晨02:00到阿斯塔纳后先在机场安全区域补觉到天亮。</li><li>10/9白天保持清醒，用城市游览撑到傍晚。</li><li>22:30 NQZ→URC航班上尽量睡；10/10凌晨到乌鲁木齐后再按当地安排补觉。</li></ol></div>
  </div>
</div></section>'''
sub_once(r'<section id="jetlag">.*?</section>', jetlag, 'jetlag')

# ---------- Checklist ----------
checklist = r'''<section id="checklist"><div class="container">
  <div class="section-head"><div><div class="eyebrow" style="color:var(--sea)">BEFORE DEPARTURE</div><h2>出发前预订与确认</h2></div><p>大交通和住宿已经基本锁定；剩下主要是景点时段和临行核验。</p></div>
  <div class="grid-2">
    <div class="card"><h3>现在还需要买 / 预约</h3><ul class="checklist"><li><b>Rijksmuseum 9/29：</b>目标10:30左右入场，优先级最高。</li><li><b>Amsterdam Canal Cruise：</b>可预留14:00左右，但尽量选可改/临近再买，避免被长途航班晚点卡死。</li><li><b>Duomo di Milano：</b>先决定是否只看外观+内部；屋顶只在你确实想近距离看建筑细节时购买，并与教堂同一次完成。</li><li><b>Truffes Folies：</b>10/2 12:00左右，如仍想吃则订位。</li><li><b>Le Bistro Dalpozzo：</b>10/4 19:00左右建议订位。</li></ul></div>
    <div class="card"><h3>出发前7天 / 24小时确认</h3><ul class="checklist"><li>CZ3802 / CZ307 实时状态，广州是否仍为联程直挂行李</li><li>Eurostar 9476：17:10发车、16:50前到站、6车64座</li><li>10/3 TGV 6177 实时状态</li><li>10/5 Nice↔Menton↔Villefranche TER班次</li><li>10/6 ZOU 602 秋季时刻，尤其Monaco→Èze与Èze→Nice</li><li>10/7 ZOU 86007 + IC631 实时站台和延误</li><li>10/8 Malpensa Express 当天时刻；J2036/J28049航站楼</li><li>10/8在MXP值机时确认托运行李在NQZ是否必须提取后重新托运</li><li>10/9 FS7961航班与NQZ最晚值机时间</li><li>旅行保险是否扩展到9/28–10/10并覆盖哈萨克斯坦</li></ul></div>
  </div>
  <div class="notice danger"><strong>已经取消，不要再按旧资料行动：</strong>Air India 上海—德里—巴黎往返已退款；10/7 Nice→Paris 夜火车已退款；10/7 Antibes 与10/8巴黎最后一天均从当前路线删除；阿姆斯特丹不住宿。</div>
  <h3 style="margin-top:28px">打包清单</h3>
  <div class="grid-3"><div class="card"><h3>随身物品</h3><ul class="checklist"><li>贴身小包/斜挎包</li><li>青旅小锁</li><li>护照复印件/电子备份</li><li>两张分开放的银行卡</li><li>少量欧元现金</li><li>阿斯塔纳清真寺用大围巾</li></ul></div><div class="card"><h3>步行装备</h3><ul class="checklist"><li>舒适步行鞋</li><li>备用薄袜</li><li>创可贴/防磨贴</li><li>轻便外套</li><li>小折伞</li></ul></div><div class="card"><h3>电子设备与应用</h3><ul class="checklist"><li>Google Maps离线区域</li><li>SNCF Connect / Eurostar</li><li>ZOU!/区域交通App</li><li>航空公司/携程订单离线截图</li><li>符合航空规则的充电宝</li></ul></div></div>
</div></section>'''
sub_once(r'<section id="checklist">.*?</section>', checklist, 'checklist')

# ---------- Alternatives ----------
alternatives = r'''<section><div class="container">
  <div class="section-head"><div><div class="eyebrow" style="color:var(--sea)">ALTERNATIVES</div><h2>突发情况备选方案</h2></div></div>
  <details open><summary>9/29 如 CZ307 晚点、进城时间被压缩</summary><div class="inside">优先保留Rijksmuseum；运河游船是第一项可删除内容。只要仍能在16:20左右回到Amsterdam Centraal，就按17:10 Eurostar执行。若出现严重延误，先查看Eurostar改签条件，不要为了游览冒误车风险。</div></details>
  <details><summary>9/29 如 Eurostar 延误导致巴黎到店较晚</summary><div class="inside">The People Bercy新增订单的入住窗口到次日00:30。出现显著晚点时，在车上/到站后尽快联系住宿说明预计抵达时间，并按实时公共交通导航前往。</div></details>
  <details><summary>10/5 如古董市场停留超时</summary><div class="inside">保留芒通老城和Sablettes海滩，适当缩短Villefranche停留时间。</div></details>
  <details><summary>10/6 如错过 Monaco→Èze 的目标公交</summary><div class="inside">先查看ZOU当日下一班；若等待时间过长，就延长摩纳哥并缩短/取消Èze，不为打卡制造危险转场。</div></details>
  <details><summary>10/7 如 Nice→Ventimiglia 明显晚点</summary><div class="inside">两段分开出票，49分钟换乘是主要缓冲。若判断赶不上09:10 IC631，立即在途中查询后续Ventimiglia→Milano列车并联系原购票渠道；不要选择07:55那种18分钟极限换乘替代。</div></details>
  <details><summary>10/9 如阿斯塔纳太疲劳或天气差</summary><div class="inside">Grand Mosque保留，其余景点按体力从National Museum、Bayterek、Khan Shatyr里删减。最晚18:00左右开始回机场，返程航班优先于城市打卡。</div></details>
</div></section>'''
sub_once(r'<section><div class="container">\s*<div class="section-head"><div><div class="eyebrow" style="color:var\(--sea\)">ALTERNATIVES</div>.*?</section>', alternatives, 'alternatives')

# ---------- Sources ----------
sources = r'''<section id="sources"><div class="container">
  <div class="section-head"><div><div class="eyebrow" style="color:var(--sea)">USEFUL LINKS</div><h2>官方与实用链接</h2></div></div>
  <div class="grid-2">
    <div class="card source-list"><h3>交通 / 票务</h3><ul>
      <li><a href="https://www.csair.com/" target="_blank">China Southern · 南航</a></li>
      <li><a href="https://www.eurostar.com/" target="_blank">Eurostar</a></li>
      <li><a href="https://www.sncf-connect.com/" target="_blank">SNCF Connect</a></li>
      <li><a href="https://www.ter.sncf.com/sud-provence-alpes-cote-d-azur/" target="_blank">TER / ZOU! Côte d’Azur</a></li>
      <li><a href="https://www.trenitalia.com/" target="_blank">Trenitalia</a></li>
      <li><a href="https://www.malpensaexpress.it/en/" target="_blank">Malpensa Express</a></li>
      <li><a href="https://www.azal.az/en" target="_blank">Azerbaijan Airlines</a></li>
    </ul></div>
    <div class="card source-list"><h3>博物馆 / 景点</h3><ul>
      <li><a href="https://www.rijksmuseum.nl/en/tickets" target="_blank">Rijksmuseum 官方票务</a></li>
      <li><a href="https://musee.louvre.fr/en/visit/hours-admission" target="_blank">Louvre</a></li>
      <li><a href="https://www.musee-orsay.fr/en/visit" target="_blank">Musée d'Orsay</a></li>
      <li><a href="https://www.explorenicecotedazur.com/en/event/marche-a-la-brocante-saleya/" target="_blank">Cours Saleya 周一古董市场</a></li>
      <li><a href="https://jardinexotique-eze.fr/en/informations/" target="_blank">Jardin Exotique d'Èze</a></li>
      <li><a href="https://www.duomomilano.it/en/" target="_blank">Duomo di Milano</a></li>
    </ul></div>
    <div class="card source-list"><h3>住宿</h3><ul>
      <li><a href="https://www.thepeoplehostel.com/en/destinations/paris-bercy/" target="_blank">The People Paris Bercy</a></li>
      <li><a href="https://slohostels.com/en/nice/" target="_blank">SLO Nice</a></li>
      <li><a href="https://www.ostelzzz.com/" target="_blank">Ostelzzz Milano</a></li>
    </ul></div>
    <div class="card source-list"><h3>餐厅 / 市场</h3><ul>
      <li><a href="https://www.thefork.com/restaurant/truffes-folies-7eme-r3597" target="_blank">Truffes Folies · TheFork</a></li>
      <li><a href="https://www.thefork.com/restaurant/le-bistro-dalpozzo-r726884" target="_blank">Le Bistro Dalpozzo · TheFork</a></li>
      <li><a href="https://www.explorenicecotedazur.com/en/shop/chez-theresa/" target="_blank">Chez Thérésa · 尼斯旅游局</a></li>
      <li><a href="https://www.boetmie.com/en/bakeries/saint-michel/" target="_blank">BO&amp;MIE Saint-Michel</a></li>
    </ul></div>
  </div>
</div></section>'''
sub_once(r'<section id="sources">.*?</section>', sources, 'sources')

# ---------- Footer / live schedule ----------
text = text.replace('<strong>法国旅行攻略 · 2026</strong><br><span style="font-size:12px">最后核验：2026-09-10。</span>', '<strong>欧洲旅行攻略 · 2026</strong><br><span style="font-size:12px">行程大改核验：2026-09-12。</span>')
text = text.replace('const tripStart = new Date(YEAR, 8, 29, 0, 0);', 'const tripStart = new Date(YEAR, 8, 28, 17, 30);')
text = text.replace('const tripEnd = new Date(YEAR, 9, 10, 3, 0);', 'const tripEnd = new Date(YEAR, 9, 10, 5, 30);')
text = text.replace("els.now.textContent = '法国行程已结束';", "els.now.textContent = '本次欧洲行程已结束';")

path.write_text(text, encoding="utf-8", newline="")
print(f"updated: {path}")
print(f"bytes: {path.stat().st_size}")
