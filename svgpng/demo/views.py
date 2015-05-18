# Create your views here.

from django import forms
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import math
import cairocffi as cairo
import io
from cairosvg import svg2png

WIDTH, HEIGHT = 256, 256


class TestForm(forms.Form):
    pass


def home(request):
    title = "SVG Title"
    body = svg(WIDTH, HEIGHT)

    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            response = HttpResponse(content_type="image/png")
            response['Content-Disposition'] = 'attachment; filename="svg.png"'
            response.write(svg2png(bytestring=body, write_to=None))
            return response
    else:
        form = TestForm()

    return render_to_response('home.html',
                              {'form': form, 'svg': {'title': title,
                                                     'body': body}},
                              context_instance=RequestContext(request))


def svg(width, height):
    imageData = io.BytesIO()
    surface = cairo.SVGSurface(imageData, width, height)
    ctx = cairo.Context(surface)

    ctx.scale(width, height)

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

    return imageData.getvalue()
