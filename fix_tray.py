lines = open('src/system_tray.py', encoding='utf-8').read().splitlines()[:405]
stop_method = ['    def stop(self):', '        """Stop the system tray"""', '        self.running = False', '        if self.icon:', '            self.icon.stop()']
open('src/system_tray.py', 'w', encoding='utf-8').write('\n'.join(lines + stop_method) + '\n')
