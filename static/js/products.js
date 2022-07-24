$('#sort-selector').change( function() {
    let selector = $(this);
    currentUrl = new URL(window.location);

    selectedValue = selector.val();
    if (selectedValue != 'reset') {
        var sort = selectedValue.split('_')[0];
        var direction = selectedValue.split('_')[1];

        currentUrl.searchParams.set('sort', sort);
        currentUrl.searchParams.set('direction', direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete('sort');
        currentUrl.searchParams.delete('direction');

        window.location.replace(currentUrl);

    }
});