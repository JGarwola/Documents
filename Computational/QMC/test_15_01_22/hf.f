      implicit none
      integer ndim,nup,ndown
      integer i
      real*8 rs,ehf
c     read(*,*)ndim,rs,nup,ndown
      ndim=2
      print*,'enter rs, nup, ndown'
      read*,rs,nup,ndown
c     do i=1,100
c      rs=1.5+0.025*i
       call hf(ndim,rs,nup,ndown,ehf)
       print*,'HF energy per particle (in Ry): ',ehf
c     enddo
c     print*,' '
c     print*,' '
      stop
      end

      subroutine hf(ndim,rs,nup,ndown,ehf)
      implicit none
c     include 'tas.cm'
      integer is,k,kp,la
      real*8 ekin,vexc,e2,q2,vmad,ehf
c     include 'pip.cm'
c     include 'cpbc.cm'
      integer nup,ndown,nppss(2),nparts,mnk,ndim,mdim,mspin
      parameter(mnk=10000,mdim=3)
      real*8 pi,rs,kmod(mnk),kvec(mdim,mnk),vol,hbs2m,el
      pi=acos(-1.d0)
      nparts=nup+ndown
      call geo(mnk,kmod,kvec,vol,el,nparts,ndim,mdim)
c     do k=1,nup
c      print*,kmod(k)
c     enddo
      mspin=1
      nppss(1)=nup
      if(ndown.gt.0)then
       mspin=2
       nppss(2)=ndown
      endif

      e2=2.d0/rs
      hbs2m=1.d0/rs**2
      ekin=0.d0
      do is=1,mspin
        do k=1,nppss(is)
          ekin=ekin+hbs2m*kmod(k)**2
        end do
      end do 
c     write(6,*)' ekin=',ekin,' ekin/N=',ekin/nparts
      vexc=0.d0
      do is=1,mspin
        do k=1,nppss(is)
          do kp=1,nppss(is)
            if(k.ne.kp) then
              q2=0.d0
              do la=1,ndim
                q2=q2+(kvec(la,k)-kvec(la,kp))**2
              end do
              if(q2.gt.1.d-8) 
     &          vexc=vexc-e2*(ndim-1.d0)*pi/q2**((ndim-1.d0)/2.d0)/vol
            end if
          end do
        end do
      end do
c     write(6,*)' vexc=',vexc,' vexc/N=',vexc/nparts
      if(ndim.eq.3)vmad=-2.837297479d0*e2/el
      if(ndim.eq.2)vmad=-3.90026492d0*e2/el
      vexc=vexc+vmad*nparts/2.d0
c     write(6,*)' vexc=',vexc,' vexc/N=',vexc/nparts
      ehf=ekin+vexc
c     write(6,*)' ehf=',ehf
c     write(6,*)' ehf/N=',ehf/nparts
      ehf=ehf/nparts
      end 
      
      subroutine geo(mnk,kmod,kvec,vol,el,nparts,ndim,mdim)
      implicit none
      integer mnk,nparts,ndim,mdim
      real*8 kmod(mnk),kvec(mdim,ndim),vol,el

      integer i,j,k,l,j_min,ng
      real*8 pi,tpiel,a,gx,gy,gz,g_min

      pi=acos(-1.d0)
      if(ndim.eq.2)then
       vol=nparts*pi
       el=vol**(1.d0/ndim)
       tpiel=2.d0*pi/el
       ng=0
       do i=-10,10
        gx=i*tpiel
        do j=-10,10
         gy=j*tpiel
         ng=ng+1
         kvec(1,ng)=gx
         kvec(2,ng)=gy
         kmod(ng)=sqrt(gx**2+gy**2)
        enddo
       enddo
      elseif(ndim.eq.3)then
       vol=nparts*4*pi/3
       el=vol**(1.d0/ndim)
       tpiel=2.d0*pi/el
       ng=0
       do i=-10,10
        gx=i*tpiel
        do j=-10,10
         gy=j*tpiel
         do k=-10,10
          gz=k*tpiel
          ng=ng+1
          kvec(1,ng)=gx
          kvec(2,ng)=gy
          kvec(3,ng)=gz
          kmod(ng)=sqrt(gx**2+gy**2+gz**2)
         enddo
        enddo
       enddo
      else
       stop'ndim'
      endif
      if(ng.gt.mnk)stop'mnk'
      do i=1,ng
       g_min=1.d10
       do j=i,ng
        if(g_min.gt.kmod(j))then
         j_min=j
         g_min=kmod(j)
        endif
       enddo
       a=kmod(i)
       kmod(i)=kmod(j_min)
       kmod(j_min)=a
       do l=1,ndim
        a=kvec(l,i)
        kvec(l,i)=kvec(l,j_min)
        kvec(l,j_min)=a
       enddo
      enddo
      return
      end
