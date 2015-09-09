var breakpoint = 1000;

jQuery(document).ready(function() {

    initForWindow();

    FeatureStyles.Camera.initialize();
    FeatureStyles.Arrow.initialize();
    FeatureStyles.FeatureImages.initialize();
    FeatureStyles.RelatedArticles.initialize();

    Search.Structure.initialize();

    Sharing.Links.initialize();

    Menu.initialize();
    
});

//initialize window based on width and height
function initForWindow(){

    FeatureStyles.MainFeatures.initializeForWindow();
    Sharing.Links.initializeForWindow();
    Header.Structure.toggleHeading();
    Header.Positioning.updateHeaderPositioning();

    $("main").click(function () {
        Menu.close();
        Search.Structure.closeBox();
        FeatureStyles.MainFeatures.removeNavigationLock();
    });
}

$(window).resize(function(){
    initForWindow();
});

$(window).scroll(function(){
    Header.Positioning.updateHeaderPositioning();
});



