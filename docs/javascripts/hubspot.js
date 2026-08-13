(function (d, s, id) {
  var e = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) {
    return;
  }
  var js = d.createElement(s);
  js.id = id;
  js.src = "//js-eu1.hs-scripts.com/145394523.js";
  e.parentNode.insertBefore(js, e);

  js.onload = function () {
    if (window.HubSpotConversations) {
      window.HubSpotConversations.widget.load();
      window.HubSpotConversations.widget.open();
    } else {
      console.warn("HubSpotConversations is not available.");
    }
  };
})(document, "script", "hs-script-loader");
