var button = $("#led_button");
button.click(function() {
    console.log(button.text());
    if (button.text() === "Red LED On") {
        $.ajax({
            url: "/led_on_r",
            type: "post",
            success: function(response) {
                console.log(response);
                button.text("Red LED Off");
            }
        });
    } else {
        $.ajax({
            url: "/led_off_r",
            type: "post",
            success: function() {
                button.text("Red LED On");
            }
        });
    }
});

var button2 = $("#led_button2");
button2.click(function() {
    console.log(button2.text());
    if (button2.text() === "Yellow LED On") {
		$.ajax({
			url:"/led_on_y",
			type: "post",
			success: function(response) {
				console.log(response);
				button2.text("Yellow LED Off");
			}
		});
    } else {
		$.ajax({
			url: "/led_off_y",
			type: "post",
			success: function() {
				button2.text("Yellow LED On");
			}
		});
	}
});

var button3 = $("#led_button3");
button3.click(function() {
    console.log(button3.text());
    if (button3.text() === "Blinking Start") {
		$.ajax({
			url:"/blink_start",
			type: "post",
			success: function(response) {
				console.log(response);
				button3.text("Blinking Stop");
			}
		});
    } else {
		$.ajax({
			url: "/blink_stop",
			type: "post",
			success: function() {
				button3.text("Blinking Start");
			}
		});
	}
});
