# Create your views here.

from django.http import HttpResponse
import math
import cairocffi as cairo
import io

WIDTH, HEIGHT = 256, 256


def demo(request):
    imageData = io.BytesIO()
    surface = cairo.SVGSurface(imageData, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    ctx.scale(WIDTH, HEIGHT)

    pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
    pat.add_color_stop_rgba(1, 0.7, 0, 0, 0.5)
    pat.add_color_stop_rgba(0, 0.9, 0.7, 0.2, 1)

    ctx.rectangle(0, 0, 1, 1)
    ctx.set_source(pat)
    ctx.fill()

    ctx.translate(0.1, 0.1)

    ctx.move_to(0, 0)
    ctx.arc(0.2, 0.1, 0.1, -math.pi/2, 0)
    ctx.line_to(0.5, 0.1)
    ctx.curve_to(0.5, 0.2, 0.5, 0.4, 0.2, 0.8)
    ctx.close_path()

    ctx.set_source_rgb(0.3, 0.2, 0.5)
    ctx.set_line_width(0.02)
    ctx.stroke()

    surface.finish()

    output = imageData.getvalue()

    response = HttpResponse(imageData.getvalue(), mimetype='image/svg+xml')
    return response
