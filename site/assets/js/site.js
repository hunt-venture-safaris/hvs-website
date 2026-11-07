/* Hunt Venture Safaris — navigation, hunt filter, enquiry form. No dependencies. */
(function () {
  'use strict';

  /* Mobile navigation */
  var nav = document.getElementById('nav');
  if (nav) {
    var toggle = nav.querySelector('.hvs-nav-toggle');
    var setOpen = function (open) {
      nav.setAttribute('data-open', String(open));
      toggle.setAttribute('aria-expanded', String(open));
    };
    toggle.addEventListener('click', function () { setOpen(nav.getAttribute('data-open') !== 'true'); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && nav.getAttribute('data-open') === 'true') { setOpen(false); toggle.focus(); } });
  }

  /* Hunts filter by month */
  var filter = document.getElementById('month-filter');
  if (filter) {
    var status = document.querySelector('.filter-status');
    filter.addEventListener('change', function () {
      var m = filter.value, shown = 0;
      document.querySelectorAll('.hunt-card[data-months]').forEach(function (card) {
        var ok = !m || card.getAttribute('data-months').split(' ').indexOf(m) > -1;
        card.hidden = !ok; if (ok) shown++;
      });
      if (status) status.textContent = m ? shown + ' / 5' : '';
    });
  }

  /* Enquiry form */
  var form = document.getElementById('enquiry');
  if (!form) return;
  var T = {};
  try { T = JSON.parse(document.getElementById('form-i18n').textContent); } catch (e) {}
  var params = new URLSearchParams(location.search);
  var pre = params.get('hunt') || params.get('species');
  if (pre) form.querySelectorAll('input[name="hunt"]').forEach(function (c) { if (c.value === pre) c.checked = true; });
  var src = params.get('source') || params.get('utm_source');
  if (src) form.querySelector('#source').value = src.slice(0, 40);

  var DRAFT = 'hvs-enquiry-draft';
  try {
    var saved = JSON.parse(sessionStorage.getItem(DRAFT) || 'null');
    if (saved) Object.keys(saved).forEach(function (k) {
      var el = form.elements[k];
      if (el && el.type !== 'checkbox' && !el.length && !el.value) el.value = saved[k];
    });
  } catch (e) {}
  form.addEventListener('input', function () {
    var d = {};
    ['name', 'email', 'phone', 'country', 'message', 'month', 'hunters', 'companions'].forEach(function (k) { if (form.elements[k]) d[k] = form.elements[k].value; });
    try { sessionStorage.setItem(DRAFT, JSON.stringify(d)); } catch (e) {}
  });

  function setError(fieldId, errId, msg) {
    var f = document.getElementById(fieldId), e = document.getElementById(errId);
    if (!f || !e) return;
    if (msg) { f.setAttribute('data-state', 'error'); e.textContent = msg; e.hidden = false; }
    else { f.removeAttribute('data-state'); e.textContent = ''; e.hidden = true; }
  }

  function buildMessage() {
    var hunts = Array.prototype.slice.call(form.querySelectorAll('input[name="hunt"]:checked')).map(function (c) { return c.getAttribute('data-label'); });
    var v = function (k) { return (form.elements[k] && form.elements[k].value || '').trim(); };
    var lines = [T.msg_intro || 'Hunt enquiry', ''];
    var add = function (label, val) { if (val) lines.push(label + ': ' + val); };
    add(T.msg_hunt, hunts.join(', '));
    add(T.msg_month, v('month'));
    add(T.msg_hunters, v('hunters'));
    add(T.msg_companions, v('companions'));
    add(T.msg_name, v('name'));
    add(T.msg_email, v('email'));
    add(T.msg_phone, v('phone'));
    add(T.msg_country, v('country'));
    if (v('source') && v('source') !== 'website') add(T.msg_source, v('source'));
    if (v('message')) { lines.push(''); lines.push(v('message')); }
    return { text: lines.join('\n'), hunts: hunts };
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var name = form.elements.name.value.trim(), email = form.elements.email.value.trim(), phone = form.elements.phone.value.trim();
    var ok = true;
    setError('fld-name', 'err-name', name ? '' : T.err_name); if (!name) ok = false;
    var emailBad = email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    setError('fld-email', 'err-email', !email && !phone ? T.err_contact : (emailBad ? T.err_email : ''));
    if ((!email && !phone) || emailBad) ok = false;
    var consent = form.elements.consent.checked;
    setError('fld-consent', 'err-consent', consent ? '' : T.err_consent); if (!consent) ok = false;
    var summary = document.getElementById('form-error');
    if (!ok) {
      summary.hidden = false; summary.focus();
      var first = form.querySelector('[data-state="error"] input');
      if (first) setTimeout(function () { first.focus(); }, 50);
      return;
    }
    summary.hidden = true;
    var msg = buildMessage();
    var endpoint = form.getAttribute('data-endpoint');
    if (endpoint) {
      var btn = form.querySelector('button[type="submit"]'); var label = btn.textContent;
      btn.disabled = true; btn.textContent = T.sending || '…';
      var fd = new FormData(form); fd.append('summary', msg.text); fd.append('hunts', msg.hunts.join(', '));
      fetch(endpoint, { method: 'POST', body: fd, headers: { 'Accept': 'application/json' } })
        .then(function (r) { if (!r.ok) throw new Error(r.status); try { sessionStorage.removeItem(DRAFT); } catch (e) {} location.href = form.getAttribute('data-thanks'); })
        .catch(function () { btn.disabled = false; btn.textContent = label; showSend(msg, T.send_failed); });
      return;
    }
    showSend(msg);
  });

  function showSend(msg, note) {
    var panel = document.getElementById('send-panel');
    document.getElementById('send-preview').textContent = msg.text;
    document.getElementById('send-wa').href = 'https://wa.me/923111667829?text=' + encodeURIComponent(msg.text);
    var subject = (T.msg_intro || 'Hunt enquiry') + (msg.hunts.length ? ' — ' + msg.hunts.join(', ') : '');
    document.getElementById('send-mail').href = 'mailto:huntventuresafaris@gmail.com?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(msg.text);
    if (note) { var p = panel.querySelector('.hvs-success p'); if (p) p.textContent = note; }
    panel.hidden = false; panel.focus();
    panel.scrollIntoView({ block: 'start', behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
  }

  var copyBtn = document.getElementById('send-copy');
  if (copyBtn) copyBtn.addEventListener('click', function () {
    var text = document.getElementById('send-preview').textContent;
    var done = function () { var span = copyBtn.lastChild; var old = span.textContent; span.textContent = ' ' + (T.copied || 'Copied'); setTimeout(function () { span.textContent = old; }, 1800); };
    if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, function () {});
  });
})();
