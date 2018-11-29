Hole in the floor
#################

:date: 2015-03-26
:tags: model
:summary: an interesting problem that I got wrong at first
:category: nullresult


An interesting question that I got wrong.  At first.

......


It's just too delicious a question to pass up.  

One of my colleagues told me a problem today, that he heard at a conference a while ago.  And he doesn't know the answer.

Someone claimed, that if you drill a hole all the way through the earth, at any angle, from any location to any other location, no matter whether or not the hole passed through the center, that if you then dropped an object down the hole, it would oscillate back and forth with the same period.

Woah.

I have no idea.

What does that even mean?  Does it even make sense?

Well this is a relative of a problem that often shows up in undergraduate physics homework:

Drill a hole through the center of the earth.  Drop an object down the hole.  What happens?

Answer: Gravity pulls the object toward the center of the earth. So it accelerates down the hole, reaching a top speed at the center, and then *slows down as it climbs back toward the surface* on the far side (because it is getting pulled toward the center).  And then it breaks the surface for a moment before falling back toward the center, and then it swings back and forth forever like a pendulum or a spring.

Of course this is assuming a lot of things that aren't true.  Like that the density of the earth is uniform.  And there's no air in this hole.  And no magma anywhere. And that the earth isn't rotating.  But that's what physicists do, so no problem.

*Naturally* I wanted to try Lagrangian dynamics.  Because why not? Write an expression for the kinetic energy.  Write an expression for the potential energy.  And write a constraint equation that keeps the particle confined to a straight line from one point on the surface to another point on the surface.

I didn't get it right.  Not sure where it went wrong, but wasn't getting a form for the equations of motion that made sense, even for the simpler case of just going straight through the center.

Then I looked at some discussions on the normal problem, the one where you drill through the center.  And was reminded of one of the most important principles in a physicist's mindtool-set:  If two situations are described by the same equations, even if the situations are totally different -- their solutions are the same.  Same idea shows up in my Algebra 2 class all the time: make your hard problem into one that you have already solved.  The classic example is the observation that an RLC circuit and a spring-mass-damper system are both described by the same differential equation.  So the solutions, which describe the behavior of real circuits and real mechanical tools, are the same.  

So what's the sister problem, whose solution is easy, that can be used to solve this one?

Turns out it's the simple harmonic oscillator (SHO).

"SHO's" are systems where the force on an object always points toward an equilibrium position, and where the magnitude of the force is proportional to the distance from that equilibrium.  Like a Hooke's law spring: :math:`F = -kx`.  The **k** is the "spring constant" for the system.  Since the force is also equal to the mass times acceleration (Newton's 2nd law), the equation of motion for the system is :math:`\ddot{x} = -\frac{k}{m}x`.  When the second derivative of a function is proportional to the function itself, the solution is a complex exponential: :math:`x(t) = A e^{-i\omega t}`, where :math:`\omega = \sqrt{\frac{k}{m}}` is the angular frequency.  Complex exponentials are equivalent to sinusoids -- periodic functions.  Their period (the time to complete one full cycle) is:

.. math::

  T = \frac{2 \pi}{\omega} & \\ 
  T = 2 \pi \sqrt{\frac{m}{k}} &
..

Notice that this period has nothing in it about how far you stretch the spring? Or really, *any* other details of the problem?  You just need the mass on the end of the spring and how strong the restoring force is.  Which is a cool result all by itself.   It's why pendulums work as time regulators, for example -- the period of a pendulum obeys a similiar equation (as long as you don't pull it too far), so it doesn't matter that you pull it back to the same angle every time, it will still swing with the same period.

Okay, so for the hole through the earth problem, what is the "k"?

The restoring force is gravity, and it depends on how far you are from the center,

.. math::

  F_c  = \frac{G M_e m_o}{r^2} & \\ 
..

(G is the universal gravitation constant, :math:`M_e` is the mass of the earth, and :math:`m_o` is the mass of the object you drop in the hole.)  This is obviously NOT a SHO.

But the mass of the earth depends on how deep you are, because you only feel a force from mass that is interior to your current radius.  If the density of the earth is uniform, then:

.. math::

  M_e =  M_{\oplus} \frac{4/3 \pi r ^3}{4/3 \pi R_{\oplus}^3} &\\
..

combining this with the expression for the force, you get:

.. math::

  F_c = \frac{G M_{\oplus} m_o}{R_{\oplus}^3} r &\\
..

which **IS** a SHO!  Because the force only depends on how far you are from the center of the earth at any moment, and it gets *bigger* the farther you are from the center.  So that means the straight-through-the-center problem has the same solution as the SHO, and all the constants having to do with the earth and gravitation make the k:

.. math::

  k = \frac{G M_{\oplus} m_o}{R_{\oplus}^3} 
..

so you can plug that into the result for period of an oscillator, and you end up getting a result of about 84.5 minutes.  Cool.

So what about the original problem, where you can drill from any point to any point and then pass straight through.  How could that *also* be a SHO, with the same **k**?

Start with the same expression for the force on the object in the hole.  It is still correct to describe the magnitude of the *total* force on the object, even if it is constrained to move in a line that doesn't pass through the center.  But just like for sliding on a ramp, we need to know the component of that total force that points along the ramp:


.. math::

  F_c = \frac{G M_{\oplus} m_o r}{R_{\oplus}^3} \sin{\theta} &\\
  \sin{\theta} = \frac{x}{r} &\\
  F_c = \frac{G M_{\oplus} m_o}{R_{\oplus}^3} x &\\
..

simple substitution of the expression for the sine of the interior angle gives the component of the total force pointing toward the center of the *path*.  And *it's proportional to the distance to the center of the path*.  Just like a SHO.  And all the constant numbers in there are *the same ones as before*.

Conclusion: it's true.  It doesn't matter where you drill the hole.

Important principles: same equations have same solutions.  Simplify *before* you solve.





