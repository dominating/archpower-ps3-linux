import re

with open('output/libsmb2-ps3/lib/sync.c', 'r') as f:
    content = f.read()

replacement = """static int wait_for_reply(struct smb2_context *smb2,
                          struct sync_cb_data *cb_data)
{
        time_t t = time(NULL);

        while (!cb_data->is_finished) {
#if defined(__PS3__) || defined(PS3_PPU_PLATFORM)
                fd_set readfds, writefds, exceptfds;
                struct timeval tv;
                int fd = smb2_get_fd(smb2);
                int events = smb2_which_events(smb2);
                int revents = 0;

                FD_ZERO(&readfds);
                FD_ZERO(&writefds);
                FD_ZERO(&exceptfds);
                if (events & POLLIN) FD_SET(fd, &readfds);
                if (events & POLLOUT) FD_SET(fd, &writefds);
                FD_SET(fd, &exceptfds);

                tv.tv_sec = 1;
                tv.tv_usec = 0;

                if (select(fd + 1, &readfds, &writefds, &exceptfds, &tv) < 0) {
                        smb2_set_error(smb2, "Select failed");
                        return -1;
                }
#else
                struct pollfd pfd;
                memset(&pfd, 0, sizeof(struct pollfd));
                pfd.fd = smb2_get_fd(smb2);
                pfd.events = smb2_which_events(smb2);

                if (poll(&pfd, 1, 1000) < 0) {
                        smb2_set_error(smb2, "Poll failed");
                        return -1;
                }
#endif
                if (smb2->timeout) {
                        smb2_timeout_pdus(smb2);
                }
                if (!SMB2_VALID_SOCKET(smb2->fd) && ((time(NULL) - t) > (smb2->timeout)))
                {
                        smb2_set_error(smb2, "Timeout expired and no connection exists\\n");
                        return -1;
                }
#if defined(__PS3__) || defined(PS3_PPU_PLATFORM)
                if (FD_ISSET(fd, &readfds)) revents |= POLLIN;
                if (FD_ISSET(fd, &writefds)) revents |= POLLOUT;
                if (FD_ISSET(fd, &exceptfds)) revents |= POLLERR;
#else
                int revents = pfd.revents;
#endif
                if (revents == 0) {
                        continue;
                }
                if (smb2_service(smb2, revents) < 0) {
                        smb2_set_error(smb2, "smb2_service failed with : "
                                        "%s\\n", smb2_get_error(smb2));
                        return -1;
                }
        }

        return 0;
}
"""

# use regex to replace wait_for_reply
pattern = re.compile(r'static int wait_for_reply\([^)]+\)\n\{.*?\n\}', re.DOTALL)
content = pattern.sub(replacement.strip(), content)

with open('output/libsmb2-ps3/lib/sync.c', 'w') as f:
    f.write(content)
